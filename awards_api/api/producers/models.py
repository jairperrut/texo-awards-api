from sqlalchemy import Column, String, Integer

from awards_api.db.engine import Base


class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer(), primary_key=True)
    name = Column(String(length=255), nullable=False)
