import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from awards_api.application import get_app
from awards_api.db.engine import Base, get_session


@pytest.fixture()
def db_session():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    with engine.begin() as connection:
        Base.metadata.drop_all(bind=connection)
        Base.metadata.create_all(bind=connection)
        with TestingSessionLocal(bind=connection) as session:
            yield session
            session.flush()
            session.rollback()


@pytest.fixture()
def override_get_session(db_session):
    def _override_get_session():
        yield db_session

    return _override_get_session


@pytest.fixture()
def app(override_get_session):
    app = get_app(init_db=False)
    app.dependency_overrides[get_session] = override_get_session
    return app


@pytest.fixture()
def client_app(app):
    return TestClient(app=app, base_url="http://test")
