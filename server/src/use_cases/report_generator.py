from typing import Iterator

from src.ai.agent import ReportCreatorAgent


class ReportGeneratorUseCase:
    def __init__(self, agent: ReportCreatorAgent):
        self.agent = agent

    def execute(self, report: str) -> str:
        return self.agent.run(report)


class ReportGeneratorStreamUseCase:
    def __init__(self, agent: ReportCreatorAgent):
        self.agent = agent

    def execute(self, report: str) -> Iterator[str]:
        response = self.agent.run_as_stream(report)

        for chunk in response:
            yield chunk
