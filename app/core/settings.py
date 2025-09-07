from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.extended_settings.app import AppSettings
from app.core.extended_settings.cors import CORSSettings
from app.core.extended_settings.database import DatabaseSettings
from app.core.extended_settings.langfuse import LangfuseSettings
from app.core.extended_settings.llm import LLMSettings


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()
    cors: CORSSettings = CORSSettings()
    llm: LLMSettings = LLMSettings()
    langfuse: LangfuseSettings = LangfuseSettings()

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

# Contoh cara akses
# settings.app.APP_NAME
# settings.llm.OPENAI_API_KEY