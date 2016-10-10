import os


class Person(object):

    def __init__(self, first_name, last_name, staff_id):
        self.first_name = first_name
        self.last_name = last_name 
        self.staff_id = staff_id
        self.allocated_office = ""
        
