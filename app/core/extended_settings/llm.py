from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    """Large Language Model API settings"""

    OPENAI_API_KEY: str = ""
    MISTRAL_API_KEY: str = ""
    TAVILY_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")