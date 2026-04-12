from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    API_VERSION: str
    SITE_NAME: str
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    model_config = SettingsConfigDict(
        env_file=".envs/.env.local",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = Settings()  # type: ignore
