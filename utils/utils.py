

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column

from sqlalchemy import Column, Integer, String




class Base(DeclarativeBase):
    pass
    # @declared_attr.cascading
    # @classmethod
    # def id(cls):
    #     for base in cls.__mro__[1:-1]:
    #         if getattr(base, "__table__", None) is not None:
    #             return mapped_column(ForeignKey(base.id), primary_key=True)
    #         else:
    #             return mapped_column(Integer, primary_key=True)


db = SQLAlchemy(model_class=Base)


class Gender(Base):
    __tablename__ = 'Gender'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)


class Kindergarten(Base):
    __tablename__ = 'Kindergarten'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)


class Group(Base):
    __tablename__ = 'Group'

    GroupID = Column(Integer, primary_key=True, autoincrement=True)
    GroupName = Column(String(255), nullable=False)
    KindergartenId = Column(Integer, ForeignKey('Kindergarten.Id'), nullable=False)


class Position(Base):
    __tablename__ = 'Position'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(255), nullable=False)


class Award(Base):
    __tablename__ = 'Award'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(255), nullable=False, unique=True)
    Description = Column(String(255), nullable=False)


class Child(Base):
    __tablename__ = 'Child'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(255), nullable=False)
    LastName = Column(String(255), nullable=False)
    GenderId = Column(Integer, ForeignKey('Gender.Id'), nullable=False)
    BirthDate = Column(DateTime, nullable=False)
    CurrentKindergartenId = Column(Integer, ForeignKey('Kindergarten.Id'), nullable=True)
    CurrentGroupId = Column(Integer, ForeignKey('Group.GroupID'), nullable=True)
    HistoryId = Column(Integer, ForeignKey('ChildHistory.Id'), nullable=False)


class ChildGroupsHistory(Base):
    __tablename__ = 'ChildGroupsHistory'

    ChildId = Column(Integer, ForeignKey('Child.Id'), primary_key=True)
    GroupId = Column(Integer, ForeignKey('Group.GroupID'), primary_key=True)


class ChildHistory(Base):
    __tablename__ = 'ChildHistory'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    AdmissionDate = Column(DateTime, nullable=False)
    GraduationDate = Column(DateTime, nullable=True)


class ChildKindergartens(Base):
    __tablename__ = 'ChildKindergartens'

    ChildId = Column(Integer, ForeignKey('Child.Id'), primary_key=True)
    KindergartenId = Column(Integer, ForeignKey('Kindergarten.Id'), primary_key=True)


class Employee(Base):
    __tablename__ = 'Employee'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(255), nullable=False)
    LastName = Column(String(255), nullable=False)
    GenderId = Column(Integer, ForeignKey('Gender.Id'), nullable=False)
    KindergartenId = Column(Integer, ForeignKey('Kindergarten.Id'), nullable=False)
    PositionId = Column(Integer, ForeignKey('Position.Id'), nullable=False)


class EmployeeAwards(Base):
    __tablename__ = 'EmployeeAwards'

    EmployeeId = Column(Integer, ForeignKey('Employee.Id'), primary_key=True)
    AwardId = Column(Integer, ForeignKey('Award.Id'), primary_key=True)


class EmployeeGroups(Base):
    __tablename__ = 'EmployeeGroups'

    CurrentGroupId = Column(Integer, ForeignKey('Group.GroupID'), primary_key=True)
    CurrentEmployeeId = Column(Integer, ForeignKey('Employee.Id'), primary_key=True)


class EmployeeHistory(Base):
    __tablename__ = 'EmployeeHistory'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    EmployeeId = Column(Integer, ForeignKey('Employee.Id'), nullable=False)
    HireDate = Column(DateTime, nullable=False)
    TerminationDate = Column(DateTime, nullable=True)



