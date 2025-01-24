from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String  # Import necessary components

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    height_cm = Column(Integer)
    city = Column(String)


class Person2(Base):
    __tablename__ = 'person2'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    height_cm = Column(Integer)
    city = Column(String)
