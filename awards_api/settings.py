from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    workers_count: int
    reload: bool = True

    debug: bool = False
    echo_db: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
