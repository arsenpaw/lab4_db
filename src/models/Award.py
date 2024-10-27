# models/award.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column

from utils.utils import Base


class Award(Base):
    __tablename__ = 'Award'

    Title = Column(String(255), nullable=False, unique=True)
    Description = Column(String(255), nullable=False)
