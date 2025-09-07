from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = "AI App"
    VERSION: str = "0.0.0-experimental"

    SITE_URL: str = "http://localhost:8000"

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="APP_", extra="ignore"
    )
