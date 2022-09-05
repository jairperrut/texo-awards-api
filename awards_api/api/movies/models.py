from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from awards_api.db.engine import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False)
    studio_id = Column(Integer, ForeignKey("studios.id"), nullable=False)
    studio = relationship("Studio")
    producer_id = Column(Integer, ForeignKey("producers.id"), nullable=False)
    producer = relationship("Producer")
