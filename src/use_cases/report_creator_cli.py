import sys

from contracts.content_handler import IContentHandler
from contracts.uploader import IUploader
from use_cases.report_creator_cli import ReportGeneratorUseCase


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

    @classmethod
    def confirm_action(self, message: str) -> bool:
        response = input(message).strip().lower()
        return response == 'y'

    def execute(self, report: str):
        first_time = True
        while True:
            message = (
                'Deseja gerar seu relatório? [Y/N]'
                if first_time
                else 'Deseja gerar novamente seu relatório? [Y/N]'
            )
            if not self.confirm_action(message):
                sys.exit()

            report_generated = self.report_generator.execute(report)
            print('######################')
            print(report_generated)

            if self.confirm_action(
                'Gostaria de fazer o upload do conteúdo para Google Drive? [Y/N]'
            ):
                filename = f'{report_generated.splitlines()[0]}'
                self.uploader.upload(report_generated, filename)
                break

            first_time = False
