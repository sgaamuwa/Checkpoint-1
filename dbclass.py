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
    current_occupants = Column(Integer, nullable=False)

class LivingSpace(Base):
    """Livingspace Database class

    This class defines database fields for the livingspace record
    """
    __tablename__ = 'livingspace'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    current_occupants = Column(Integer, nullable=False)

class Staff(Base):
    """Staff Database class

    This class defines database fields for the staff record
    """
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    office_id = Column(Integer, ForeignKey('office.id'), nullable=True)
    office = relationship(Office)

class Fellow(Base):
    """Fellow Database class

    This class defines database fields for the fellow record
    """
    __tablename__ = 'fellow'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    office_id = Column(Integer, ForeignKey('office.id'), nullable=True)
    livingspace_id = Column(Integer, ForeignKey('livingspace.id'), nullable=True)
    office = relationship(Office)
    livingspace = relationship(LivingSpace)

engine = create_engine('sqlite:///amity_db')

Base.metadata.create_all(engine)