from typing import Iterator

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

from src.ai.llm import llm
from src.ai.template import template_instructions


class ReportCreatorAgent:
    def run(self, report_data: str) -> str:
        prompt_template = ChatPromptTemplate.from_template(template_instructions)
        chain = prompt_template | llm | StrOutputParser()

        return chain.invoke({'report': report_data})

    def run_as_stream(self, report_data: str) -> Iterator[str]:
        prompt_template = ChatPromptTemplate.from_template(template_instructions)

        chain = prompt_template | llm | StrOutputParser()

        return chain.stream({'report': report_data})
