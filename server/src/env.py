from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    ENV_MODE: Optional[str] = 'dev'
    OPEN_AI_KEY: str
    OPEN_AI_BASE_URL: str
    CHAT_MODEL: str
    EMBEDDING_MODEL: str
    DRIVE_FOLDER_ID: str
    DISCORD_CHANNEL_ID: str
    DISCORD_TOKEN: str

    GOOGLE_SERVICE_ACCOUNT_TYPE: str
    GOOGLE_PROJECT_ID: str
    GOOGLE_PRIVATE_KEY_ID: str
    GOOGLE_PRIVATE_KEY: str
    GOOGLE_CLIENT_EMAIL: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_AUTH_URI: str
    GOOGLE_TOKEN_URI: str
    GOOGLE_AUTH_PROVIDER_X509_CERT_URL: str
    GOOGLE_CLIENT_X509_CERT_URL: str

    DATABASE_URL: str
    JWT_SECRET: str

    SUPABASE_URL: str
    SUPABASE_KEY: str
    STORAGE_BUCKET: str


env = Env()
