import logging
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    # Application
    PROJECT_NAME: str = "Twaice RTE Metrics"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = "v1"
    DEBUG: bool = True

    # Task queue
    TASK_BROKER_URL: str = "amqp://guest@task-queue//"
    TASK_BACKEND_URL: str = "db+sqlite:///db.sqlite3"

    class Config:
        env_file = "twaice_rte/.env"
        env_prefix = "TWAICE_RTE_"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
