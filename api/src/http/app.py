from http import HTTPStatus

from crewai import Crew
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.ai.agent import report_writer
from src.ai.report_writer import writer
from src.http.dtos.generate_report_response import GenerateReportResponse
from src.http.dtos.response import Message
from src.http.dtos.upload_report_request import UploadReportRequest
from src.http.dtos.upload_report_response import UploadReportResponse
from src.repositories.discord_repository import DiscordRepository
from src.repositories.google_drive_repository import GoogleDriveRepository
from src.use_cases.report_creator_api import ReportCreatorUseCase
from src.use_cases.report_generator import ReportGeneratorUseCase

app = FastAPI()

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

content_repository = DiscordRepository()
uploader_repository = GoogleDriveRepository()
crew = Crew(agents=[report_writer], tasks=[writer], verbose=2)
report_generator = ReportGeneratorUseCase(crew)
report_creator = ReportCreatorUseCase(
    content_repository, report_generator, uploader_repository
)


@app.post(
    '/generate-report',
    status_code=HTTPStatus.CREATED,
    response_model=GenerateReportResponse,
)
def generate_report():
    content = content_repository.get_content()
    response = report_creator.execute(content)
    return JSONResponse(
        status_code=HTTPStatus.CREATED,
        content={'report': response.raw},
    )


@app.post(
    '/upload-report',
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
