import re
import uuid
from http import HTTPStatus

import chardet
from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

from src.ai.agent import ReportCreatorAgent
from src.auth.current_user import CurrentUser
from src.database.models import ReportModel
from src.database.repositories.discord_repository import DiscordRepository
from src.database.repositories.google_drive_repository import GoogleDriveRepository
from src.database.repositories.report_repository import ReportRepository
from src.database.repositories.supabase_repository import SupabaseRepository
from src.http.common.dtos.response import Message
from src.http.routes.reports.dtos.upload_report_request import UploadReportRequest
from src.http.routes.reports.dtos.upload_report_response import UploadReportResponse
from src.lib.supabase import supabase
from src.use_cases.create_report import CreateReportUseCase
from src.use_cases.fetch_reports_from_user import FetchReportsFromUserUseCase
from src.use_cases.report_generator import (
    ReportGeneratorStreamUseCase,
)

router = APIRouter(prefix='/reports', tags=['reports'])


content_repository = DiscordRepository()
uploader_repository = GoogleDriveRepository()
report_repository = ReportRepository()
supabase_repository = SupabaseRepository(supabase)
agent = ReportCreatorAgent()
report_generator_stream = ReportGeneratorStreamUseCase(agent, content_repository)
fetch_reports_from_user_use_case = FetchReportsFromUserUseCase(report_repository)
create_report_use_case = CreateReportUseCase(report_repository, uploader_repository)


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
    try:
        result = create_report_use_case.execute(body, user_id=user.id)

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


@router.post(path='/sync')
def process_files_in_drive_folder(user: CurrentUser):
    files = uploader_repository.list_files_in_folder()
    for file in files:
        file_id = file['id']
        file_name = file['name']
        mime_type = file['mimeType']
        downloaded_file = uploader_repository.download_file(file_id, mime_type)
        downloaded_file.seek(0)  # Ensure we're reading from the start of the stream
        content_bytes = downloaded_file.read()

        # Detectar a codificação do conteúdo
        result = chardet.detect(content_bytes)
        encoding = result['encoding']

        if not encoding:
            raise UnicodeDecodeError('Não foi possível detectar a codificação do arquivo')

        content = content_bytes.decode(encoding)
        word_count = len(re.findall(r'\w+', content))
        upload_response = supabase_repository.upload_to_supabase(content_bytes, file_name)
        report = ReportModel(
            id=str(uuid.uuid4()),
            title=file_name,
            file_id=upload_response.id,
            word_count=word_count,
            user_id=user.id,
            storage_url=upload_response.url,
        )
        report_repository.save(report)
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={'message': 'Arquivos salvos com sucesso!'},
    )
