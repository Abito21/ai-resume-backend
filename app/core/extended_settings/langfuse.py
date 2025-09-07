from pydantic_settings import BaseSettings, SettingsConfigDict


class LangfuseSettings(BaseSettings):
    """Langfuse observability settings"""

    LANGFUSE_SECRET_KEY: str = ""
    LANGFUSE_PUBLIC_KEY: str = ""
    LANGFUSE_HOST: str = ""

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="LANGFUSE_", extra="ignore"
    )
