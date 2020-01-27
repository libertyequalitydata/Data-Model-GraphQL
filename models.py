from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Basic(Base):
    __tablename__ = 'basic'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    highesteducation = Column(String)
    basic_id = Column(Integer, ForeignKey('basic.id'))
    basic = relationship(
        Basic,
        backref=backref('educations',
                        uselist=True,
                        cascade='delete,all'))

class Occupation(Base):
    __tablename__ = 'occupation'
    id = Column(Integer, primary_key=True)
    organization = Column(String)
    employeedepartment = Column(String)
    employeeprimaryrole = Column(String)
    basic_id = Column(Integer, ForeignKey('basic.id'))
    basic = relationship(
        Basic,
        backref=backref('occupations',
                        uselist=True,
                        cascade='delete,all'))

class Household(Base):
    __tablename__ = 'household'
    id = Column(Integer, primary_key=True)
    numberofpersonsinhome = Column(Integer)
    maritalstatus = Column(String)
    numberofchildren = Column(Integer)
    accomodationtype = Column(String)
    income = Column(Integer)
    basic_id = Column(Integer, ForeignKey('basic.id'))
    basic = relationship(
        Basic,
        backref=backref('households',
                        uselist=True,
                        cascade='delete,all'))
