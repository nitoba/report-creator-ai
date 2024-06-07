from os import path

from agent import report_writer, writer
from crewai import Crew
from repositories.file_handler_repository import FileHandlerRepository
from repositories.google_drive_repository import GoogleDriveRepository
from use_cases.report_creator import ReportCreatorUseCase
from use_cases.report_generator import ReportGeneratorUseCase

if __name__ == '__main__':
    print('Bem-vindo ao Report Creator AI')
    file_directory = path.join(path.dirname(__file__), '../tmp/')
    file_handler = FileHandlerRepository(file_directory)
    crew = Crew(agents=[report_writer], tasks=[writer], verbose=2)
    report_generator = ReportGeneratorUseCase(crew)
    uploader = GoogleDriveRepository()

    report_creator = ReportCreatorUseCase(file_handler, report_generator, uploader)
    content = file_handler.get_content('report.txt')
    report_creator.generate_and_upload_report(content)
