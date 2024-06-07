import sys
from os import path

from agent import report_writer, writer
from crewai import Crew
from upload import upload_from_content_to_drive

crew = Crew(
    agents=[report_writer],
    tasks=[writer],
    verbose=2,
)


file_report = path.join(path.dirname(__file__), '../tmp/')


def generate_ai_report(report: str, is_first_time=True):
    message = (
        'Deseja gerar seu relatório? [Y/N]'
        if is_first_time
        else 'Deseja gerar novamente seu relatório? [Y/N]'
    )
    confirm = input(message)

    if confirm.strip().lower() == 'y':
        report_generated = crew.kickoff(inputs={'report': report})
        print('######################')
        print(report_generated)

        confirm_upload_result = input(
            'Gostaria de fazer o upload do conteúdo para Google Drive? [Y/N]'
        )

        if confirm_upload_result.strip().lower() == 'y':
            upload_report(report_generated)
        if confirm_upload_result.strip().lower() == 'n':
            generate_ai_report(report, False)
    if confirm.strip().lower() == 'n':
        sys.exit()


def upload_report(content: str):
    file_name = f'{content.splitlines()[0]}'
    upload_from_content_to_drive(content, file_name)


print('Bem-vindo ao Report Creator AI')

with open(file_report + 'report.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    generate_ai_report(content)
