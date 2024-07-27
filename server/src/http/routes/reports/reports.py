from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

from src.ai.agent import ReportCreatorAgent
from src.database.repositories.discord_repository import DiscordRepository
from src.database.repositories.google_drive_repository import GoogleDriveRepository
from src.http.common.dtos.response import Message
from src.http.routes.reports.dtos.generate_report_response import GenerateReportResponse
from src.http.routes.reports.dtos.upload_report_request import UploadReportRequest
from src.http.routes.reports.dtos.upload_report_response import UploadReportResponse
from src.use_cases.report_creator_api import ReportCreatorUseCase
from src.use_cases.report_generator import (
    ReportGeneratorStreamUseCase,
    ReportGeneratorUseCase,
)

router = APIRouter(prefix='/reports', tags=['reports'])


content_repository = DiscordRepository()
uploader_repository = GoogleDriveRepository()
agent = ReportCreatorAgent()
report_generator = ReportGeneratorUseCase(agent)
report_generator_stream = ReportGeneratorStreamUseCase(agent)
report_creator = ReportCreatorUseCase(
    content_repository, report_generator, uploader_repository
)


@router.post(
    '/generate',
    status_code=HTTPStatus.CREATED,
    response_model=GenerateReportResponse,
)
def generate_report():
    print('Generating report...')
    content = content_repository.get_content()
    response = report_creator.execute(content)
    if not response:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={'message': 'Error generating report'},
        )

    return JSONResponse(
        status_code=HTTPStatus.CREATED,
        content={'report': response},
    )


@router.get(
    '/generate/stream',
    status_code=HTTPStatus.CREATED,
)
def generate_report_stream():
    print('Generating report...')
    content = content_repository.get_content()
    response = report_creator.execute(content)
    if not response:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={'message': 'Error generating report'},
        )

    return StreamingResponse(
        report_generator_stream.execute(response), media_type='text/plain'
    )


@router.post(
    '/upload',
    status_code=HTTPStatus.OK,
    response_model=UploadReportResponse,
    responses={
        HTTPStatus.BAD_REQUEST: {
            'description': 'Error uploading report',
            'model': Message,
        },
    },
)
def upload_report(body: UploadReportRequest):
    if not body.title:
        body.title = f'{body.content.splitlines()[0]}'

    try:
        result = uploader_repository.upload(filename=body.title, content=body.content)
        return {'message': result}
    except Exception as err:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={'message': f'Error uploading report: {err}'},
        )
