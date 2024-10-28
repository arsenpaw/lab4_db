from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from utils.utils import db


class Repository:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def add(self, entity):
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def update(self, entity):
        try:
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def delete(self, entity):
        try:
            db.session.delete(entity)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
