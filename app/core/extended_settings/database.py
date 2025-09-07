from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5441
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "postgres"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6381

    @property
    def DB_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="DB_", extra="ignore")
    # Gunakan config bawah apabila terdapat DB_ di dalam .env sehingga hapus bagian env_prefix
    # model_config = SettingsConfigDict(env_file=".env", extra="ignore")
