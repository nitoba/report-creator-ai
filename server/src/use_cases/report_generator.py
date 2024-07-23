from src.ai.agent import ReportCreatorAgent


class ReportGeneratorUseCase:
    def __init__(self, agent: ReportCreatorAgent):
        self.agent = agent

    def execute(self, report: str) -> str:
        return self.agent.run(report)
