# models/gender.py

from sqlalchemy import Column, Integer, String

from utils.utils import db, Base


class Gender(Base):
    __tablename__ = 'Gender'
    Name = Column(String(255), nullable=False)
