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
    highestdegree = Column(String)
    areaofstudy = Column(String)
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
    income = Column(String)
    basic_id = Column(Integer, ForeignKey('basic.id'))
    basic = relationship(
        Basic,
        backref=backref('households',
                        uselist=True,
                        cascade='delete,all'))

class Foodandbeverage(Base):
    __tablename__ = 'foodandbeverage'
    id = Column(Integer, primary_key=True)
    fastfoodweeklyfrequency = Column(Integer)
    alcoholweeklyfrequency = Column(Integer)
    restaurantweeklyfrequency = Column(Integer)
    basic_id = Column(Integer, ForeignKey('basic.id'))
    basic = relationship(
        Basic,
        backref=backref('foodandbeverages',
                        uselist=True,
                        cascade='delete,all'))

class Hobbiesandinterests(Base):
    __tablename__ = 'hobbiesandinterests'
    id = Column(Integer, primary_key=True)
    cinemaweeklyfrequency = Column(Integer)
    exerciseweeklyfrequency = Column(Integer)
    favoritemusicgenre = Column(String)
    basic_id = Column(Integer, ForeignKey('basic.id'))
    basic = relationship(
        Basic,
        backref=backref('hobbiesandinterests',
                        uselist=True,
                        cascade='delete,all'))
