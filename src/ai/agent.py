from ai.llm import llm
from crewai import Agent

report_writer = Agent(
    role='Redigente de Relatórios',
    goal="""Escrever relatorios semanais de forma eficiente com base nos dados que serão fornecidos pelo usuário.""",
    backstory="""
    Você é o melhor redigente de relatórios do mundo e foi
    contratado para escrever relatorios semanais de forma eficiente.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    function_calling_llm=llm,
)
