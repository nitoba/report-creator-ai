from crewai import Crew


class ReportGeneratorUseCase:
    def __init__(self, crew: Crew):
        self.crew = crew

    def generate_report(self, report: str) -> str:
        return self.crew.kickoff(inputs={'report': report})
