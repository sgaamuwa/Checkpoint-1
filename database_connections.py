from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dbclass import Staff 
from dbclass import Fellow 
from dbclass import Office
from dbclass import LivingSpace

engine = create_engine('sqlite:///amity_db')

Base = declarative_base()

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def database_insert_staff(fname, lname, dept, title, office_id):
    """Insertion function

    This function inputs new staff into the database
    """
    new_staff = Staff(first_name=fname, last_name=lname, department=dept, title=title, office_id=office_id)
    session.add(new_staff)
    session.commit()

def database_insert_fellow(fname, lname, cohort, level, office_id, livingspace_id):
    """Insertion function

    This function inputs new fellow into the database
    """
    new_fellow = Staff(first_name=fname, last_name=lname, cohort=cohort, level=level, office_id=office_id, livingspace_id=livingspace_id)
    session.add(new_fellow)
    session.commit()

def database_insert_office(name):
    """Insertion function

    This function inputs a new office into the database
    """
    new_office = Office(name=name, current_occupants=0)
    session.add(new_office)
    session.commit()

def database_insert_livingspace(name):
    """Insertion function

    This function inputs a new livingspace into the database
    """
    new_livingspace = LivingSpace(name=name, current_occupants=0)
    session.add(new_livingspace)
    session.commit()
