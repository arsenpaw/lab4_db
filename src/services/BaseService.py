from src.repository.BaseRepository import Repository


class BaseService:
    def __init__(self, model):
        self.repository = Repository(model)

    def _to_dict(self, entity):
        """Convert a SQLAlchemy model instance into a dictionary."""
        return {c.name: getattr(entity, c.name) for c in entity.__table__.columns}

    def get_by_id(self, id):
        entity = self.repository.get_by_id(id)
        return self._to_dict(entity) if entity else None

    def get_all(self):
        entities = self.repository.get_all()
        return [self._to_dict(entity) for entity in entities]

    def create(self, entity_data):
        entity = self.repository.model(**entity_data)
        saved_entity = self.repository.add(entity)
        return self._to_dict(saved_entity)

    def update(self, id, update_data):
        entity = self.repository.get_by_id(id)
        if not entity:
            return None
        for key, value in update_data.items():
            setattr(entity, key, value)
        updated_entity = self.repository.update(entity)
        return self._to_dict(updated_entity)

    def delete(self, id):
        entity = self.repository.get_by_id(id)
        if not entity:
            return None
        self.repository.delete(entity)
        return True
