import os 

from rooms.office import Office
from rooms.livingspace import LivingSpace

class Amity(object):

    def __init__(self):
        pass 

    def create_room(name, type):
        """creates a room depending on the type specified"""

        if type = "office":
            room = Office(name)
            room.save()
        elif type ="livingspace":
            room = LivingSpace(name)
            room.save()

    def assign_room(person):
        """randomly assigns a room to the person that it is passed"""
        return "" 

    def reallocate(person, room):
        """assigns a person to the specified room if it is free"""
        pass

    def print_allocations():
        """returns a printout of all rooms and persons assigned to them"""
        return "" 

    def save_state(database):
        """saves current system data in a specified database"""
        pass 

    def load_state(database):
        """loads data from a specified database into the system"""
        pass 

    def load_people(filename):
        """loads people into the system from specified file"""
        pass 