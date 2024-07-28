from src.contracts.uploader import IUploader
from src.database.models import ReportModel
from src.database.repositories.report_repository import ReportRepository
from src.http.routes.reports.dtos.upload_report_request import UploadReportRequest


class CreateReportUseCase:
    def __init__(self, report_repository: ReportRepository, uploader: IUploader):
        self.report_repository = report_repository
        self.uploader = uploader

    def execute(self, request: UploadReportRequest) -> None:
        try:
            if not request.title:
                request.title = f'{request.content.splitlines()[0]}'

            result = self.uploader.upload(
                filename=request.title,
                content=request.content,
            )

            report = ReportModel(
                title=request.title,
                file_id=result.id,
                user_id=request.user_id,
                storage_url=result.url,
                word_count=len(request.content.split()),
            )

            self.report_repository.save(report)

            return {'message': result}
        except Exception as e:
            print(f'Error creating report: {e}')
