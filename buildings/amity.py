import os 
import random

from database.database_connections import DatabaseConnections
from people.fellow import Fellow
from people.staff import Staff
from rooms.office import Office
from rooms.livingspace import LivingSpace



class Amity(object):

    staff = {}
    fellows = {}
    offices = {}
    livingspaces = {}

    def create_room(name, kind):
        """creates a room depending on the type specified"""
        #create room object respectively
        if kind == "office":
            room = Office(name)
            Amity.offices[name] = room
        elif kind == "livingspace":
            room = LivingSpace(name)
            Amity.livingspaces[name] = room

    def add_person(fname, lname, title, wants_accommodation=None):
        """creates a new person basing on their specified type"""

        if title == "FELLOW":
            person = Fellow(fname, lname)
            Amity.assign_room(person)
            if wants_accommodation == "Y":
                Amity.assign_livingspace(person)
            Amity.fellows[person.staff_id] = person
        if title == "STAFF":
            person = Staff(fname, lname)
            Amity.assign_room(person)
            Amity.staff[person.staff_id] = person
        
        return "{} {} allocated to {}".format(person.first_name, person.last_name,
                                                person.allocated_office)

    def assign_room(person):
        """randomly assigns a room to the person that it is passed"""
        #create available rooms and append rooms with space to it 
        if len(Amity.offices) == 0:
            return "There are no rooms"
        available_offices = []
        for office in Amity.offices.values():
            if len(office.current_occupants) < 6:
                available_offices.append(office)
        #if there are no free rooms
        if len(available_offices) == 0:
            return "All current rooms are full"
        else:
            random_office = random.choice(available_offices)
        person.allocated_office = random_office.name
        random_office.current_occupants.append(person.first_name +" "+ person.last_name)
        Amity.offices[random_office.name] = random_office
    
    def assign_livingspace(person):
        """randomly assigns a room to the person that it is passed"""
        #create available rooms and append rooms with space to it 
        if len(Amity.livingspaces) == 0:
            return "There are no rooms"
        available_livingspaces = []
        for livingspace in Amity.livingspaces.values():
            if len(livingspace.current_occupants) < 4:
                available_livingspaces.append(livingspace)
        #if there are no free rooms
        if len(available_livingspaces) == 0:
            return "All current rooms are full"
        else:
            random_livingspace = random.choice(available_livingspaces)
        person.allocated_livingspace = random_livingspace.name
        random_livingspace.current_occupants.append(person.first_name 
                                                +" "+ person.last_name)
        Amity.livingspaces[random_livingspace.name] = random_livingspace

    def reallocate(person, room_name):
        """assigns a person to the specified room if it is free"""
        #check for the room in the rooms list 
        if name in Amity.offices.keys():
            office = Amity.offices[room_name]
        else:
            return "Room doesn't exist"
        #if the room is full
        if len(office.current_occupants) == 6:
            return "The room is full"
        elif person.allocated_office == room_name:
            return "Already allocated to room"
        #remove the person from their current office
        Amity.offices[person.allocated_office].current_occupants.remove(person.first_name +" "
                                                                        + person.last_name)
        person.allocated_office = office.room_name
        office.current_occupants.append(person.first_name +" "+ person.last_name)

    def print_allocations(filename=None):
        """returns a printout of all rooms and persons assigned to them"""
        #check if the filename is empty and print on the screen
        if filename == None:
            for office in Amity.offices.values():
                print(office.name+"\n")
                print("-"*70)
                print("\n")
                for person in office.current_occupants:
                    print(person+", ", end="\n")
                print("\n\n")
            for livingspace in Amity.livingspaces.values():
                print(livingspace.name+"\n")
                print("-"*70)
                print("\n")
                for person in livingspace.current_occupants:
                    print(person+", ", end="\n") 
                print("\n\n")
        else:
            #write out to the filename listed
            with open("../datafiles/"+filename, "w") as output:
                for office in Amity.offices.values():
                    output.write(office.name+"\n")
                    output.write("-"*70)
                    output.write("\n")
                    for person in office.current_occupants:
                        output.write(person+", ", end="\n")
                    output.write("\n\n")
                for livingspace in Amity.livingspaces.values():
                    output.write(livingspace.name+"\n")
                    output.write("-"*70)
                    output.write("\n")
                    for person in livingspace.current_occupants:
                        output.write(person+", ", end="\n") 
                    output.write("\n\n")
    
    def print_unallocated(filename=None):
        """returns a list of all the unallocated staff members"""
        unallocated = []
        #add the unallocated to a list
        for person in Amity.staff.values():
            if person.allocated_office == "":
                unallocated.append(person.first_name +" "+ person.last_name)
        for person in Amity.fellows.values():
            if person.allocated_office == "":
                unallocated.append(person.first_name +" "+ person.last_name)
        for person in unallocated:
            if filename == None:
                print(person)
            else:
                with open("../datafiles/"+filename, "w") as output:
                    output.write(person)

    def save_state(database_name=None):
        """saves current system data in a specified database"""
        if database_name == None:
            database = DatabaseConnections("amity_db")
        else:
            database = DatabaseConnections(database_name)
        for room in Amity.livingspaces.values():
            database.database_insert_livingspace(room.name, room.current_occupants)

    def load_state(database):
        """loads data from a specified database into the system"""
        database = DatabaseConnections(database)
        for row in database.database_return_all_offices:
            Amity.offices[row.name] = row
        for row in database.database_return_all_livingspaces:
            Amity.livingspaces[row.name] = row
        for row in database.database_return_all_fellows:
            Amity.fellows[row.staff_id] = row
        for row in database.database_return_all_staff:
            Amity.staff[row.staff_id] = row 

    def load_people(filename):
        """loads people into the system from specified file"""
        people = []
        with open("../datafiles/"+filename) as data:
            input = data.readlines()
            #for each line splits them into their individual words
            for line in input:
                if line:
                    person = line.split()
                    people.append(person)
        for person in people:
            if len(person) == 4:
                Amity.add_person(person[0], person[1], person[2], person[3])
            else:
                Amity.add_person(person[0], person[1], person[2])

Amity.create_room("python", "livingspace")
Amity.save_state()

