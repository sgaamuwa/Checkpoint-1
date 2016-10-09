import os

from buildings.amity import Amity
from people.staff import Staff


class Person(object):

    def __init__(self, first_name, last_name, staff_id):
        self.first_name = first_name
        self.last_name = last_name 
        self.staff_id = staff_id
        self.allocated_office = ""

    @staticmethod       
    def request_reallocation(staff_id, room):
        if staff_id in Amity.staff.keys():
            person = Amity.reallocate(Amity.staff[staff_id], room)
            Amity.staff[staff_id] = person
        elif staff_id in Amity.fellows.keys():
            person = Amity.reallocate(Amity.fellows[staff_id], room)
            Amity.fellows[staff_id] = person
         

    @staticmethod
    def print_unallocated():
        unallocated = []
        for person in Amity.staff.values():
            if person.allocated_office == "":
                unallocated.append(person.first_name + person.last_name)
        for person in Amity.fellows.values():
            if person.allocated_office == "":
                unallocated.append(person.first_name + person.last_name)
        
