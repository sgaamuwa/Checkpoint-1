from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database.dbclass import Staff 
from database.dbclass import Fellow 
from database.dbclass import Office
from database.dbclass import LivingSpace

class DatabaseConnections(object):

    engine = create_engine('sqlite:///amity_db')

    Base = declarative_base()

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    def set_database(name):
        """Creates a new engine
        
        changes the engine to a new specified database 
        """
        DatabaseConnections.engine = create_engine("sqlite:///{}".format(name))

    def database_insert_staff(fname, lname, office_id):
        """Insertion function

        This function inputs new staff into the database
        """
        new_staff = Staff(first_name=fname, last_name=lname)
        DatabaseConnections.session.add(new_staff)
        DatabaseConnections.session.commit()

    def database_insert_fellow(fname, lname, office_id, livingspace_id):
        """Insertion function

        This function inputs new fellow into the database
        """
        new_fellow = Fellow(first_name=fname, last_name=lname, office_id=office_id, livingspace_id=livingspace_id)
        DatabaseConnections.session.add(new_fellow)
        DatabaseConnections.session.commit()

    def database_insert_office(name):
        """Insertion function

        This function inputs a new office into the database
        """
        new_office = Office(name=name, current_occupants=0)
        DatabaseConnections.session.add(new_office)
        DatabaseConnections.session.commit()

    def database_insert_livingspace(name):
        """Insertion function

        This function inputs a new livingspace into the database
        """
        new_livingspace = LivingSpace(name=name, current_occupants=0)
        DatabaseConnections.session.add(new_livingspace)
        DatabaseConnections.session.commit()

    def database_delete_staff(fname, lname):
        """Deletion function

        This function deletes a specified staff from the database
        """
        DatabaseConnections.session.query(Staff).filter_by(first_name=fname, last_name=lname).delete()
        DatabaseConnections.session.commit()

    def database_delete_fellow(fname, lname):
        """Deletion function

        This function delete a specified fellow from the database
        """
        DatabaseConnections.session.query(Fellow).filter_by(first_name=fname, last_name=lname).delete()
        DatabaseConnections.session.commit()

    def database_delete_office(name):
        """Deletion function

        This function delete a specified office from the database
        """
        DatabaseConnections.session.query(Office).filter_by(name=name).delete()
        DatabaseConnections.session.commit()

    def database_delete_livingspace(name):
        """Deletion function

        This function delete a specified livingspace from the database
        """
        DatabaseConnections.session.query(LivingSpace).filter_by(name=name).delete()
        DatabaseConnections.session.commit()

    def database_update_staff(fname, lname, office_name):
        """Update function

        This function updates the office of a staff in the database
        """
        office = DatabaseConnections.session.query(Office).filter_by(name=office_name).first()
        staff = DatabaseConnections.session.query(Staff).filter_by(first_name=fname, last_name=lname).first()
        staff.office_id = office.id
        DatabaseConnections.session.commit()

    def database_update_fellow(fname, lname, office_name):
        """Update function

        This function updates the office or livingspace of a fellow in the database
        """
        office = DatabaseConnections.session.query(Office).filter_by(name=office_name).first()
        fellow = DatabaseConnections.session.query(Fellow).filter_by(first_name=fname, last_name=lname).first()
        fellow.office_id =office.id
        DatabaseConnections.session.commit()
        #find a way to include the livingspace as well

    def database_update_office(name):
        """Update function

        This function updates the occupants in an office in the database
        """
        office = DatabaseConnections.session.query(Office).filter_by(name=name).first()
        office.current_occupants += 1
        DatabaseConnections.session.commit()

    def database_update_livingspace(name):
        """Update function

        This function updates the occupants in a livingspace in the database
        """
        livingspace = DatabaseConnections.session.query(LivingSpace).filter_by(name=name).first()
        livingspace.current_occupants += 1
        DatabaseConnections.session.commit()

    def database_return_all_staff():
        """Retrieve function

        This function returns all staff members in the database
        """
        results = []
        rows = DatabaseConnections.session.query(Staff).all()
        for row in rows:
            results.append((row.id, row.first_name, row.last_name,
            row.office_id))
        return results

    def database_return_all_fellows():
        """Retrieve function

        This function returns all fellows in the database
        """
        results = []
        rows = DatabaseConnections.session.query(Fellow).all()
        for row in rows:
            results.append((row.id, row.first_name, row.last_name,
            row.office_id, row.livingspace_id))
        return results

    def database_return_staff(fname, lname):
        """Retrieve function

        This function returns a specified staff member from the database
        """
        row = DatabaseConnections.session.query(Staff).filter_by(first_name=fname, last_name=lname).first()
        if row is not None:
            return (row.id, row.first_name, row.last_name, row.office_id)
        else:
            return "Does Not Exist"

    def database_return_fellow(fname, lname):
        """Retrieve function

        This function returns a specified fellow from the database
        """
        row = DatabaseConnections.session.query(Fellow).filter_by(first_name=fname, last_name=lname).first()
        if row is not None:
            return (row.id, row.first_name, row.last_name, row.office_id, row.livingspace_id)
        else:
            return "Does Not Exist"

    def database_return_all_offices(name):
        """Retrieve function

        This function returns all offices in the database
        """
        results = []
        rows = DatabaseConnections.session.query(Office).all()
        for row in rows:
            results.append((row.id, row.name, row.current_occupants))
        return results

    def database_return_all_livingspaces(name):
        """Retrieve function

        This function returns all livingspaces in the database
        """
        results = []
        rows = DatabaseConnections.session.query(Office).all()
        for row in rows:
            results.append((row.id, row.name, row.current_occupants))
        return results

    def database_return_office(name):
        """Retrieve function

        This function returns a specified office from the database
        """
        row = DatabaseConnections.session.query(Office).filter_by(name=name).first()
        if row is not None:
            return (row.id, row.name, row.current_occupants)
        else:
            return "Does not exist"

    def database_return_livingspace(name):
        """Retrieve function

        This function returns a specified livingspace from the database
        """
        row = DatabaseConnections.session.query(LivingSpace).filter_by(name=name).first()
        if row is not None:
            return (row.id, row.name, row.current_occupants)
        else:
            return "Does not exist"
