from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from src.env import env

if env.ENV_MODE == 'dev':
    llm = ChatOllama(
        model=env.CHAT_MODEL,
        temperature=0.5,
        base_url=env.OPEN_AI_BASE_URL,
    )
    # llm = ChatOpenAI(
    #     model=env.CHAT_MODEL,
    #     temperature=0.5,
    #     api_key=env.OPEN_AI_KEY,
    #     base_url=env.OPEN_AI_BASE_URL,
    # )
else:
    llm = ChatGroq(
        api_key=env.OPEN_AI_KEY,
        model=env.CHAT_MODEL,
        temperature=0.5,
    )
