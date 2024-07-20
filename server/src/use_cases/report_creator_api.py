from src.contracts.content_handler import IContentHandler
from src.contracts.uploader import IUploader
from src.use_cases.report_generator import ReportGeneratorUseCase


class ReportCreatorUseCase:
    def __init__(
        self,
        content_handler: IContentHandler,
        report_generator: ReportGeneratorUseCase,
        uploader: IUploader,
    ):
        self.content_handler = content_handler
        self.report_generator = report_generator
        self.uploader = uploader

    def execute(self, report: str) -> str:
        report_generated = self.report_generator.execute(report)
        return report_generated
