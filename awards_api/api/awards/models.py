from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from awards_api.db.engine import Base


class Award(Base):
    __tablename__ = "awards"

    id = Column(Integer(), primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    movie = relationship("Movie")
    year = Column(Integer(), nullable=False)
    winner = Column(Boolean(), nullable=False)
