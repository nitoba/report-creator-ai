from src.contracts.uploader import IUploader
from src.database.models import ReportModel
from src.database.repositories.report_repository import ReportRepository
from src.http.routes.reports.dtos.upload_report_request import UploadReportRequest


class CreateReportUseCase:
    def __init__(self, report_repository: ReportRepository, uploader: IUploader):
        self.report_repository = report_repository
        self.uploader = uploader

    def execute(self, request: UploadReportRequest, user_id: str) -> None:
        try:
            if not request.title:
                lines = request.content.splitlines()
                lines.remove('')
                request.title = lines[0].removeprefix('**').removesuffix('**')

            result = self.uploader.upload(
                filename=request.title,
                content=request.content,
            )

            report = ReportModel(
                title=request.title,
                file_id=result.id,
                user_id=user_id,
                storage_url='https://www.url.com',
                word_count=len(request.content.split()),
            )

            self.report_repository.save(report)

            return 'Report created successfully'
        except Exception as e:
            print(f'Error creating report: {e}')
