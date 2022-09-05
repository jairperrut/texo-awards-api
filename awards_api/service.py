from awards_api.repository import Repository


class CRUDService:

    def __init__(self, session, model):
        self.repository = Repository(session, model)

    def find(self, filters: dict = {}):
        return self.repository.find(filters).all()

    def find_by_id(self, pk: int):
        return self.repository.find_by_id(pk)

    def get_or_create(self, data):
        return self.repository.get_or_create(data)

    def create(self, data):
        return self.repository.create(data)

    def update(self, pk: int, data: dict):
        return self.repository.update(pk, data)
