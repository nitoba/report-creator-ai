from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

from src.ai.agent import ReportCreatorAgent
from src.auth.current_user import CurrentUser
from src.database.repositories.discord_repository import DiscordRepository
from src.database.repositories.google_drive_repository import GoogleDriveRepository
from src.database.repositories.report_repository import ReportRepository
from src.http.common.dtos.response import Message
from src.http.routes.reports.dtos.upload_report_request import UploadReportRequest
from src.http.routes.reports.dtos.upload_report_response import UploadReportResponse
from src.use_cases.create_report import CreateReportUseCase
from src.use_cases.fetch_reports_from_user import FetchReportsFromUserUseCase
from src.use_cases.report_generator import (
    ReportGeneratorStreamUseCase,
)

router = APIRouter(prefix='/reports', tags=['reports'])


content_repository = DiscordRepository()
uploader_repository = GoogleDriveRepository()
report_repository = ReportRepository()
agent = ReportCreatorAgent()
report_generator_stream = ReportGeneratorStreamUseCase(agent, content_repository)
fetch_reports_from_user_use_case = FetchReportsFromUserUseCase(report_repository)
create_report_use_case = CreateReportUseCase(report_repository, uploader_repository)


# @router.post(
#     '/generate',
#     status_code=HTTPStatus.CREATED,
#     response_model=GenerateReportResponse,
# )
# def generate_report():
#     print('Generating report...')
#     content = content_repository.get_content()
#     response = report_creator.execute(content)
#     if not response:
#         return JSONResponse(
#             status_code=HTTPStatus.BAD_REQUEST,
#             content={'message': 'Error generating report'},
#         )

#     return JSONResponse(
#         status_code=HTTPStatus.CREATED,
#         content={'report': response},
#     )


@router.get(
    '/generate/stream',
    status_code=HTTPStatus.CREATED,
)
def generate_report_stream(user: CurrentUser):
    stream_response = report_generator_stream.execute()
    if not stream_response:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={'message': 'Error generating report'},
        )

    return StreamingResponse(stream_response, media_type='text/plain')


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
def upload_report(body: UploadReportRequest, user: CurrentUser):
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


@router.get(
    path='',
    status_code=HTTPStatus.OK,
    response_model=list,
)
def fetch_reports_from_user(user: CurrentUser):
    return fetch_reports_from_user_use_case.execute(user.id)
