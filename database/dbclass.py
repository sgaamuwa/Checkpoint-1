import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Office(Base):
    """Office Database class

    This class defines database fields for the office record
    """
    __tablename__ = 'office'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)

class LivingSpace(Base):
    """Livingspace Database class

    This class defines database fields for the livingspace record
    """
    __tablename__ = 'livingspace'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)

class Staff(Base):
    """Staff Database class

    This class defines database fields for the staff record
    """
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    allocated_office = Column(String(250), ForeignKey('office.name'), nullable=True)
    office = relationship(Office)

class Fellow(Base):
    """Fellow Database class

    This class defines database fields for the fellow record
    """
    __tablename__ = 'fellow'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    allocated_office = Column(String(250), ForeignKey('office.name'), nullable=True)
    allocated_livingspace = Column(String(250), ForeignKey('livingspace.name'), nullable=True)
    office = relationship(Office)
    livingspace = relationship(LivingSpace)

def generate_db(database_name):
    """generate a database based on the name given"""

    engine = create_engine("sqlite:///{}".format(database_name))

    Base.metadata.create_all(engine)