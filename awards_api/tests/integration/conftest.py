import factory
import pytest
from factory.fuzzy import FuzzyInteger

from awards_api.api.studios.models import Studio
from awards_api.api.producers.models import Producer
from awards_api.api.movies.models import Movie
from awards_api.api.awards.models import Award


@pytest.fixture
def studio_factory(db_session):
    class StudioFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Studio
            sqlalchemy_session = db_session

        id = factory.Sequence(lambda n: n)
        name = factory.Sequence(lambda n: 'Studio %d' % n)

    return StudioFactory


@pytest.fixture
def producer_factory(db_session):
    class ProducerFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Producer
            sqlalchemy_session = db_session

        id = factory.Sequence(lambda n: n)
        name = factory.Sequence(lambda n: 'Producer %d' % n)

    return ProducerFactory


@pytest.fixture
def movie_factory(db_session, producer_factory, studio_factory):
    class MovieFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Movie
            sqlalchemy_session = db_session

        id = factory.Sequence(lambda n: n)
        title = factory.Sequence(lambda n: 'Movie %d' % n)
        studio = factory.SubFactory(studio_factory)
        producer = factory.SubFactory(producer_factory)

    return MovieFactory


@pytest.fixture
def award_factory(db_session, movie_factory):
    class AwardFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Award
            sqlalchemy_session = db_session

        id = factory.Sequence(lambda n: n)
        year = FuzzyInteger(1980, 2010)
        movie = factory.SubFactory(movie_factory)
        winner = False

    return AwardFactory
