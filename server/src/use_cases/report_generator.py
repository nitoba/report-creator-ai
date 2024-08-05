from typing import Iterator

from src.ai.agent import ReportCreatorAgent
from src.contracts.content_handler import IContentHandler


class ReportGeneratorStreamUseCase:
    def __init__(self, agent: ReportCreatorAgent, content_handler: IContentHandler):
        self.agent = agent
        self.content_handler = content_handler

    def execute(self) -> Iterator[str] | None:
        content = self.content_handler.get_content()

        if not content:
            return None

        response = self.agent.run_as_stream(content)

        for chunk in response:
            print(chunk, end='', flush=True)
            yield chunk
