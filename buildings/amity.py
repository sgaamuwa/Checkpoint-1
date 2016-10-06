import os 

from rooms.office import Office
from rooms.livingspace import LivingSpace

class Amity(object):

    def __init__(self):
        pass 

    def create_room(name, type):
        if type = "office":
            room = Office(name)
            room.save()
        elif type ="livingspace":
            room = LivingSpace(name)
            room.save()

    def assign_room(person):
        return "" 

    def reallocate(person, room):
        pass

    def print_allocations():
        return "" 

    def save_state(database):
        pass 

    def load_state(database):
        pass 

    def load_people(filename):
        pass 