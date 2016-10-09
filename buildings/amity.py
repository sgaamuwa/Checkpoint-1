import os 
import random

from rooms.office import Office
from rooms.livingspace import LivingSpace
from people.fellow import Fellow
from people.staff import Staff
from database.database_connections.DatabaseConnections import (database_return_office, 
    database_update_fellow, database_update_staff, 
    database_update_office, set_database,
    database_return_all_fellows, database_return_all_staff, 
    database_return_all_livingspaces, database_return_all_offices)

class Amity(object):

    staff = {}
    fellows = {}
    offices = {}
    livingspaces = {}

    def __init__(self):
        """initialises class, appending data from database to working set"""
        pass

    def create_room(name, room_id, kind):
        """creates a room depending on the type specified"""
        #create room object respectively
        if kind == "office":
            room = Office(name)
            Amity.offices[room_id] = room
        elif kind == "livingspace":
            room = LivingSpace(name)
            Amity.livingspaces[room_id] = room

    def add_person(fname, lname, staff_id, type):
        """creates a new person basing on their specified type"""

        if type == "FELLOW":
            person = Fellow(fname, lname, staff_id)
            Amity.assign_room(person)
            fellows[staff_id] = person
        if type == "STAFF":
            person = Staff(fname, lname, staff_id)
            Amity.assign_room(person)
            staff[staff_id] = person
        
        return "{} {} allocated to {}".format(person.first_name, person.last_name,
                                                person.allocated_office)

    def assign_room(person):
        """randomly assigns a room to the person that it is passed"""
        #create available rooms and append rooms with space to it 
        if len(Amity.offices) == 0:
            return "There are no rooms"
        available_offices = []
        for office in Amity.offices.values():
            if room.current_occupants < 6:
                available_offices.append(office)
        #if there are no free rooms
        if len(available_offices) == 0:
            return "All current rooms are full"
        else:
            random_office = available_offices[random.randint(0, (len(available_offices) - 1))]
        person.allocated_office = random_office.room_id

    def reallocate(person, room_name):
        """assigns a person to the specified room if it is free"""
        #check for the room in the rooms list 
        if room_name in Amity.offices.keys():
            office = Amity.offices["room_name"]
        else:
            return "Room doesn't exist"
        #if the room is full
        if office.current_occupants == 6:
            return "The room is full"
        person.allocated_office = office.room_id
        office.current_occupants += 1
        return person

    def print_allocations():
        """returns a printout of all rooms and persons assigned to them"""
        return "" 

    def save_state(database):
        """saves current system data in a specified database"""
        pass 

    def load_state(database):
        """loads data from a specified database into the system"""
        if database is not None:
            set_database(database)
        for row in database_return_all_offices:
           Amity.rooms
        for row in database_return_all_livingspaces:
            Amity.rooms.append({row.name : row})
        for row in database_return_all_fellows:
            Amity.people.append({row.staff_id : row})
        for row in database_return_all_staff:
            Amity.people.append({row.staff_id : row})

    def load_people(filename):
        """loads people into the system from specified file"""
        pass 