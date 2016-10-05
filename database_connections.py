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
    new_fellow = Fellow(first_name=fname, last_name=lname, cohort=cohort, level=level, office_id=office_id, livingspace_id=livingspace_id)
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

def database_delete_staff(fname, lname):
    """Deletion function

    This function deletes a specified staff from the database
    """
    session.query(Staff).filter_by(first_name=fname, last_name=lname).delete()
    session.commit()

def database_delete_fellow(fname, lname):
    """Deletion function

    This function delete a specified fellow from the database
    """
    session.query(Fellow).filter_by(first_name=fname, last_name=lname).delete()
    session.commit()

def database_delete_office(name):
    """Deletion function

    This function delete a specified office from the database
    """
    session.query(Office).filter_by(name=name).delete()
    session.commit()

def database_delete_livingspace(name):
    """Deletion function

    This function delete a specified livingspace from the database
    """
    session.query(LivingSpace).filter_by(name=name).delete()
    session.commit()

def database_update_staff(fname, lname, office_name):
    """Update function

    This function updates the office of a staff in the database
    """
    office = session.query(Office).filter_by(name=office_name).first()
    staff = session.query(Staff).filter_by(first_name=fname, last_name=lname).first()
    staff.office_id = office.id
    session.commit()

def database_update_fellow(fname, lname, office_name):
    """Update function

    This function updates the office or livingspace of a fellow in the database
    """
    office = session.query(Office).filter_by(name=office_name).first()
    fellow = session.query(Fellow).filter_by(first_name=fname, last_name=lname).first()
    fellow.office_id =office.id
    session.commit()
    #find a way to include the livingspace as well

def database_update_office(name):
    """Update function

    This function updates the occupants in an office in the database
    """
    office = session.query(Office).filter_by(name=name).first()
    office.current_occupants += 1
    session.commit()

def database_update_livingspace(name):
    """Update function

    This function updates the occupants in a livingspace in the database
    """
    livingspace = session.query(LivingSpace).filter_by(name=name).first()
    livingspace.current_occupants += 1
    session.commit()

def database_return_all_staff():
    """Retrieve function

    This function returns all staff members in the database
    """
    results = []
    rows = session.query(Staff).all()
    for row in rows:
        results.append((row.id, row.first_name, row.last_name,
        row.department, row.title, row.office_id))
    return results

def database_return_all_fellows():
    """Retrieve function

    This function returns all fellows in the database
    """
    results = []
    rows = session.query(Fellow).all()
    for row in rows:
        results.append((row.id, row.first_name, row.last_name,
        row.cohort, row.level, row.office_id, row.livingspace_id))
    return results

def database_return_staff(fname, lname):
    """Retrieve function

    This function returns a specified staff member from the database
    """
    row = session.query(Staff).filter_by(first_name=fname, last_name=lname).first()
    return (row.id, row.first_name, row.last_name, row.department, row.title,
            row.office_id)

def database_return_fellow(fname, lname):
    """Retrieve function

    This function returns a specified fellow from the database
    """
    row = session.query(Fellow).filter_by(first_name=fname, last_name=lname).first()
    return (row.id, row.first_name, row.last_name, row.cohort, row.level,
            row.office_id, row.livingspace_id)

def database_return_all_offices(name):
    """Retrieve function

    This function returns all offices in the database
    """
    results = []
    rows = session.query(Office).all()
    for row in rows:
        results.append((row.id, row.name, row.current_occupants))
    return results

def database_return_all_livingspaces(name):
    """Retrieve function

    This function returns all livingspaces in the database
    """
    results = []
    rows = session.query(Office).all()
    for row in rows:
        results.append((row.id, row.name, row.current_occupants))
    return results

def database_return_office(name):
    """Retrieve function

    This function returns a specified office from the database
    """
    row = session.query(Staff).filter_by(name=name).first()
    return (row.id, row.name, row.current_occupants)

def database_return_livingspace(fname, lname):
    """Retrieve function

    This function returns a specified livingspace from the database
    """
    row = session.query(Staff).filter_by(name=name).first()
    return (row.id, row.name, row.current_occupants)

print(database_return_fellow())
database_update_fellow("Samuel", "Gaamuwa", "narnia")
print(database_return_fellow())