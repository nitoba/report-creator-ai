from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

from src.ai.llm import llm
from src.ai.template import template_instructions


class ReportCreatorAgent:
    def run(self, report_data: str):
        prompt_template = ChatPromptTemplate.from_template(template_instructions)
        chain = prompt_template | llm | StrOutputParser()

        return chain.invoke({'report': report_data})
