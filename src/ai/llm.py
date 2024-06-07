from env import Env
from langchain_openai import ChatOpenAI

env = Env()

llm = ChatOpenAI(
    api_key=env.OPEN_AI_KEY,
    model=env.CHAT_MODEL,
    temperature=0.5,
    base_url=env.OPEN_AI_BASE_URL,
)
