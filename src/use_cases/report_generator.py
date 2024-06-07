from crewai import Crew


class ReportGeneratorUseCase:
    def __init__(self, crew: Crew):
        self.crew = crew

    def execute(self, report: str) -> str:
        return self.crew.kickoff(inputs={'report': report})
