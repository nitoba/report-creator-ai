import sys

from ai.agent import report_writer
from ai.report_writer import writer
from crewai import Crew
from repositories.discord_repository import DiscordRepository
from repositories.google_drive_repository import GoogleDriveRepository
from use_cases.report_generator import ReportGeneratorUseCase

from src.use_cases.report_creator_cli import ReportCreatorUseCase

if __name__ == '__main__':
    print('Bem-vindo ao Report Creator AI')
    crew = Crew(agents=[report_writer], tasks=[writer], verbose=2)

    content_repository = DiscordRepository()
    uploader_repository = GoogleDriveRepository()

    report_generator = ReportGeneratorUseCase(crew)
    report_creator = ReportCreatorUseCase(
        content_repository, report_generator, uploader_repository
    )

    content = content_repository.get_content()
    if len(content) == 0:
        print('Conteúdo não encontrado por favor verifique a fonte de dados!')
        sys.exit(0)
    report_creator.execute(content)
