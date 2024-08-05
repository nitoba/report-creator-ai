import uuid
from datetime import datetime

from src.contracts.uploader import IUploader
from src.database.models import ReportModel
from src.database.repositories.report_repository import ReportRepository
from src.database.repositories.supabase_repository import SupabaseRepository
from src.http.routes.reports.dtos.upload_report_request import UploadReportRequest


class CreateReportUseCase:
    def __init__(
        self,
        report_repository: ReportRepository,
        uploader: IUploader,
        supabase_repository: SupabaseRepository,
    ):
        self.report_repository = report_repository
        self.supabase_repository = supabase_repository
        self.uploader = uploader

    def execute(self, request: UploadReportRequest, user_id: str, user_email: str) -> str:
        try:
            if not request.title:
                lines = request.content.splitlines()
                lines.remove('')
                request.title = lines[0].removeprefix('**').removesuffix('**')

            if not request.content:
                raise ValueError('Content is required')

            if user_email == 'bruno.santos@tegra.com.br':
                self.uploader.upload(
                    filename=request.title,
                    content=request.content,
                )

            result_upload = self.supabase_repository.upload_to_supabase(
                request.content.encode(), request.title
            )

            report = ReportModel(
                id=str(uuid.uuid4()),
                title=request.title,
                file_id=result_upload.id,
                user_id=user_id,
                storage_url=result_upload.url,
                word_count=len(request.content.split()),
                created_at=datetime.now(),
            )

            self.report_repository.save(report)

            return 'Report created successfully'
        except Exception as e:
            print(f'Error creating report: {e}')
