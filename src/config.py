from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=Path(__file__).parent/".env", extra="ignore")


settings = AppSettings()
print(settings.DATABASE_URL)
