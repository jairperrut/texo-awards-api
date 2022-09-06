from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    workers_count: int
    reload: bool = True

    log_level: str = "INFO"
    debug: bool = False
    echo_db: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "awards_api": {"handlers": ["default"], "level": settings.log_level},
    },
}