from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    API_VERSION: str
    SITE_NAME: str
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DRIVER: str = "asyncpg"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_RESULT_DB: int = 1
    MAIL_FROM: str = ""
    MAIL_FORM_NAME: str = ""
    SMTP_HOST: str = "mailpit"
    SMTP_PORT: int = 1025
    MAILPIT_PORT: int = 8025
    # RABBITMQ is not configured in the docker-compose.yml file. but i will add it later to be the celery broker driver and redis will be for only the result backend
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"

    model_config = SettingsConfigDict(
        env_file=".envs/.env.local",
        env_ignore_empty=True,
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def REDIS_BROKER_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    @property
    def REDIS_BACKEND_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_RESULT_DB}"

    @property
    def RABBITMQ_BROKER_URL(self) -> str:
        return f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}//"


settings = Settings()  # type: ignore
