from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from awards_api.db.engine import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False, unique=True)
    studios = relationship("Studio", secondary="movies_studios_association")
    producers = relationship("Producer", secondary="movies_producers_association")


movies_producers_association = Table(
    "movies_producers_association",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("producer_id", ForeignKey("producers.id"), primary_key=True),
)

movies_studios_association = Table(
    "movies_studios_association",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("studio_id", ForeignKey("studios.id"), primary_key=True),
)
