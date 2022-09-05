from sqlalchemy.orm import Session
from sqlalchemy import update

from awards_api.db.engine import Base


class Repository:

    def __init__(self, session: Session, model: Base):
        self.session = session
        self.model = model

    def find(self, filters):
        return self.session.query(self.model).filter_by(**filters)

    def find_by_id(self, pk):
        return self.session.query(self.model).filter(self.model.id == pk).first()

    def get_or_create(self, data):
        instance = self.find(filters=data).first()
        if instance:
            return instance
        return self.create(data)

    def create(self, data: dict):
        db_data = self.model(**data)
        self.session.add(db_data)
        self.session.commit()
        self.session.refresh(db_data)
        return db_data

    def update(self, pk, data: dict):
        self.session.execute(
            update(self.model).
            where(self.model.id == pk).
            values(**data)
        )
        self.session.commit()
        return self.find_by_id(pk)
