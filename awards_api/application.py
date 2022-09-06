from logging.config import dictConfig
from fastapi import FastAPI

from awards_api.settings import log_config
from awards_api.db.engine import SessionLocal
from awards_api.router import api_routers
from awards_api.api.awards.service import AwardService


def get_app(init_db=True) -> FastAPI:
    dictConfig(log_config)

    app = FastAPI(
        title="Texo Awards API",
        description="FastAPI service for Texo Awards",
        version="0.0.1"
    )

    app.include_router(router=api_routers)
    if init_db:
        load_movies_csv()

    return app


def load_movies_csv():
    try:
        session = SessionLocal()
        AwardService(session).load_from_csv('movielist.csv')
    finally:
        session.close()
