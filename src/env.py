from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    OPEN_AI_KEY: str
    OPEN_AI_BASE_URL: str
    CHAT_MODEL: str
    EMBEDDING_MODEL: str
    REDIS_URL: str
    DRIVE_FOLDER_ID: str


env = Env()
