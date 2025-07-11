import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = os.getenv("POSTGRES_HOST")
    DB_PORT: int = os.getenv("POSTGRES_PORT")
    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_DRIVER: str = os.getenv("POSTGRES_DRIVER")
    DB_NAME: str = os.getenv("POSTGRES_DB")

    KAFKA_SERVER: str = os.getenv("KAFKA_SERVER")
    EVENT_TYPE_PROCESS_SWIPES: str = os.getenv("EVENT_TYPE_PROCESS_SWIPES")
    PROCESS_SWIPES_TOPIC: str = os.getenv("PROCESS_SWIPES_TOPIC")

    @property
    def db_url(self):
        return (f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
