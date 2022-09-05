from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from awards_api.settings import settings

SQLALCHEMY_DATABASE_URL = "sqlite:///./texo_awards.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=settings.echo_db
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    try:
        session = SessionLocal()
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
