from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database.dbclass import Staff 
from database.dbclass import Fellow 
from database.dbclass import Office
from database.dbclass import LivingSpace
from database.dbclass import generate_db

class DatabaseConnections(object):

    def __init__(self, database_name="amity_db"):
        self.create_database(database_name)
        self.engine = create_engine("sqlite:///{}".format(database_name))
        self.Base = declarative_base()
        self.Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()
    
    def create_database(self, database_name):
        """create a new database or use system described database"""

        generate_db(database_name)

    def database_insert_staff(self, fname, lname, allocated_office):
        """Insertion function

        This function inputs new staff into the database
        """
        new_staff = Staff(first_name=fname, last_name=lname, 
                            allocated_office=allocated_office)
        self.session.add(new_staff)
        self.session.commit()

    def database_insert_fellow(self, fname, lname, office, livingspace):
        """Insertion function

        This function inputs new fellow into the database
        """
        new_fellow = Fellow(first_name=fname, last_name=lname, 
                            allocated_office=office, 
                            allocated_livingspace=livingspace)
        self.session.add(new_fellow)
        self.session.commit()

    def database_insert_office(self, name):
        """Insertion function

        This function inputs a new office into the database
        """
        new_office = Office(name=name)
        self.session.add(new_office)
        self.session.commit()

    def database_insert_livingspace(self, name):
        """Insertion function

        This function inputs a new livingspace into the database
        """
        new_livingspace = LivingSpace(name=name)
        self.session.add(new_livingspace)
        self.session.commit()

    def database_delete_staff(self, fname, lname):
        """Deletion function

        This function deletes a specified staff from the database
        """
        self.session.query(Staff).filter_by(first_name=fname, last_name=lname).delete()
        self.session.commit()

    def database_delete_fellow(self, fname, lname):
        """Deletion function

        This function delete a specified fellow from the database
        """
        self.session.query(Fellow).filter_by(first_name=fname, last_name=lname).delete()
        self.session.commit()

    def database_delete_office(self, name):
        """Deletion function

        This function delete a specified office from the database
        """
        self.session.query(Office).filter_by(name=name).delete()
        self.session.commit()

    def database_delete_livingspace(self, name):
        """Deletion function

        This function delete a specified livingspace from the database
        """
        self.session.query(LivingSpace).filter_by(name=name).delete()
        self.session.commit()

    def database_update_staff(self, fname, lname, office):
        """Update function

        This function updates the office of a staff in the database
        """
        staff = self.session.query(Staff).filter_by(first_name=fname, last_name=lname).first()
        staff.allocated_office = office
        self.session.commit()

    def database_update_fellow(self, fname, lname, office, livingspace):
        """Update function

        This function updates the office or livingspace of a fellow in the database
        """
        fellow = self.session.query(Fellow).filter_by(first_name=fname, last_name=lname).first()
        fellow.allocated_office =office
        fellow.allocated_livingspace = livingspace
        self.session.commit()

    def database_return_all_staff(self):
        """Retrieve function

        This function returns all staff members in the database
        """
        results = []
        rows = self.session.query(Staff).all()
        for row in rows:
            results.append((row.first_name, row.last_name,
            row.allocated_office))
        return results

    def database_return_all_fellows(self):
        """Retrieve function

        This function returns all fellows in the database
        """
        results = []
        rows = self.session.query(Fellow).all()
        for row in rows:
            results.append((row.first_name, row.last_name,
            row.allocated_office, row.allocated_livingspace))
        return results

    def database_return_all_offices(self, name):
        """Retrieve function

        This function returns all offices in the database
        """
        results = []
        rows = self.session.query(Office).all()
        for row in rows:
            results.append((row.name))
        return results

    def database_return_all_livingspaces(self, name):
        """Retrieve function

        This function returns all livingspaces in the database
        """
        results = []
        rows = self.session.query(Office).all()
        for row in rows:
            results.append((row.name))
        return results
