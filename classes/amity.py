import os 
import random

from database.database_connections import DatabaseConnections
from classes.person import Fellow
from classes.person import Staff
from classes.room import Office
from classes.room import LivingSpace


class Amity(object):

    staff = {}
    fellows = {}
    offices = {}
    livingspaces = {}

    def create_room(name, kind):
        """creates a room depending on the type specified"""

        #sheck if room is already in the system
        if (name.lower() in (key.lower() for key in Amity.offices.keys()) 
        or name.lower() in (key.lower() for key in Amity.livingspaces.keys())):
            return "Room already exists"
        #create room object and add it to respective dictionary
        elif kind == "office":
            room = Office(name)
            Amity.offices[name] = room
        elif kind == "livingspace":
            room = LivingSpace(name)
            Amity.livingspaces[name] = room
        return "Room {} has been created".format(name)

    def add_person(fname, lname, title, wants_accommodation=None):
        """creates a new person basing on their specified type"""

        staff_id = input("Enter {} {}'s staff id: ".format(fname, lname))
        #calls the validate staff id to ensure it is unique
        Amity.validate_staff_id(staff_id)
        #check if the person is staff or fellow
        if title == "FELLOW":
            person = Fellow(fname, lname, staff_id)
            Amity.assign_room(person)
            #if wants accommodation assign livingspace
            if wants_accommodation == "Y":
                Amity.assign_livingspace(person)
            Amity.fellows[person.staff_id] = person
        if title == "STAFF":
            person = Staff(fname, lname, staff_id)
            Amity.assign_room(person)
            Amity.staff[person.staff_id] = person
        
        return "{} {} added and assigned to {}".format(person.first_name, 
                                person.last_name, person.allocated_office)

    def validate_staff_id(staff_id):
        """determines that the staff id is not in the system"""

        if staff_id in Amity.fellows.keys() or staff_id in Amity.staff.keys():
            print("Staff Id already exists")
            staff_id = input("Enter another staff id: ")
            Amity.validate_staff_id(staff_id) 
    
    def add_fellow_from_database(fname, lname, staff_id, office=None, livingspace=None):
        """adds a fellow from the database to the working dataset"""

        #create a Fellow object of person from the database
        fellow = Fellow(fname, lname, staff_id)
        fellow.allocated_livingspace = livingspace
        fellow.allocated_office = office
        Amity.fellows[fellow.staff_id] = fellow
        #add person to office they are allocated to in the database
        if office is not "" and office is not None:
            Amity.offices[office].current_occupants.append(staff_id+" "+fname+" "+lname)
        #add person to livingspace they are allocated to in database
        if livingspace is not "" and livingspace is not None:
            Amity.livingspaces[livingspace].current_occupants.append(staff_id+" "+fname+" "+lname)

    def add_staff_from_database(fname, lname, staff_id, office=None):
        """adds a fellow from the database to the working dataset"""

        #create a Staff object of person from the database
        staff = Staff(fname, lname, staff_id)
        staff.allocated_office = office
        Amity.staff[staff.staff_id] = staff
        #add person to allocated room 
        if office is not "" and office is not None:
            Amity.offices[office].current_occupants.append(staff_id+" "+fname+" "+lname)

    def assign_room(person):
        """randomly assigns a room to the person that it is passed"""

        #create available rooms and append rooms with space to it 
        if len(Amity.offices) == 0:
            return "There are no rooms"
        #list for the available offices
        available_offices = []
        for office in Amity.offices.values():
            if len(office.current_occupants) < 6:
                available_offices.append(office)
        #if there are no free rooms
        if len(available_offices) == 0:
            return "All current rooms are full"
        else:
            #randomise the choice of the office 
            random_office = random.choice(available_offices)
        person.allocated_office = random_office.name
        random_office.current_occupants.append(person.staff_id+" "
                        +person.first_name +" "+ person.last_name)
        #update the room object in the dictionaries 
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
            #randomise the choice of the livingspace
            random_livingspace = random.choice(available_livingspaces)
        person.allocated_livingspace = random_livingspace.name
        random_livingspace.current_occupants.append(person.staff_id+" "+person.first_name 
                                                +" "+ person.last_name)
        #update the room object in the dictionary
        Amity.livingspaces[random_livingspace.name] = random_livingspace

    def reallocate(person, room_name):
        """assigns a person to the specified room if it is free"""

        #check for the room in the rooms list 
        if room_name in Amity.offices.keys():
            office = Amity.offices[room_name]
        else:
            return "Room doesn't exist"
        #if the room is full
        if len(office.current_occupants) == 6:
            return "The room is full"
        elif person.allocated_office == room_name:
            return "Already allocated to room"
        #remove the person from their current office
        Amity.offices[person.allocated_office].current_occupants.remove(person.staff_id+" "
                                                    +person.first_name +" "+ person.last_name)
        person.allocated_office = office.name
        #add person to the new selected office
        office.current_occupants.append(person.staff_id+" "+person.first_name +" "+ person.last_name)
        return "{} {} reallocated to {}".format(person.first_name, 
                                        person.last_name, office.name)
    
    def reallocate_ls(person, room_name):
        """assigns a person to the specified room if it is free"""

        #check for the room in the rooms list 
        if room_name in Amity.livingspaces.keys():
            lspace = Amity.livingspaces[room_name]
        else:
            return "Room doesn't exist"
        #if the room is full
        if len(lspace.current_occupants) == 6:
            return "The room is full"
        elif person.allocated_livingspace == room_name:
            return "Already allocated to room"
        #remove the person from their current livingspace
        Amity.livingspaces[person.allocated_livingspace].current_occupants.remove(person.staff_id+" "
                                                            +person.first_name +" "+ person.last_name)
        person.allocated_livingspace = lspace.name
        #add person to the new selected livingspace
        lspace.current_occupants.append(person.staff_id+" "+person.first_name +" "+ person.last_name)
        return "{} {} reallocated to {}".format(person.first_name, 
                                        person.last_name, lspace.name)

    def print_allocations(filename=None):
        """returns a printout of all rooms and persons assigned to them"""

        #check if there are rooms to display in the system
        if len(Amity.offices) == 0 and len(Amity.livingspaces) == 0:
            return "There are no rooms in the system"
        #check if the filename is empty and print on the screen
        if filename == None:
            for office in Amity.offices.values():
                print(office.name+"(office)\n")
                print("-"*80)
                print("\n")
                for person in office.current_occupants:
                    print(person+", ", end=" ")
                print("\n\n")
            for livingspace in Amity.livingspaces.values():
                print(livingspace.name+"(livingspace)\n")
                print("-"*80)
                print("\n")
                for person in livingspace.current_occupants:
                    print(person+", ", end=" ") 
                print("\n\n")
        else:
            #write out to the filename listed
            with open("./datafiles/"+filename, "w") as output:
                for office in Amity.offices.values():
                    output.write(office.name+"(office)\n")
                    output.write("-"*70)
                    output.write("\n")
                    for person in office.current_occupants:
                        output.write(person+", ")
                    output.write("\n\n")
                for livingspace in Amity.livingspaces.values():
                    output.write(livingspace.name+"(livingspace)\n")
                    output.write("-"*70)
                    output.write("\n")
                    for person in livingspace.current_occupants:
                        output.write(person+", ") 
                    output.write("\n\n")
        return "Rooms all printed"
    
    def print_unallocated(filename=None):
        """prints a list of all the unallocated staff members"""

        unallocated = []
        #add the unallocated to a list
        for person in Amity.staff.values():
            if person.allocated_office == "":
                unallocated.append(person.first_name +" "+ person.last_name)
        for person in Amity.fellows.values():
            if person.allocated_office == "":
                unallocated.append(person.first_name +" "+ person.last_name)
        if len(unallocated) == 0:
            return "There are no unallocated persons"
        for person in unallocated:
            if filename == None:
                print("Unallocated Office:")
                print(person)
            else:
                #write out to the specified file 
                with open("./datafiles/"+filename, "w") as output:
                    output.write("Unallocated Office")
                    output.write(person)

    def save_state(database_name=None):
        """saves current system data in a specified database"""

        if database_name == None:
            #set the default database to amity_db
            database = DatabaseConnections("amity_db")
        else:
            #otherwise use the specified name
            database = DatabaseConnections(database_name)
        for room in Amity.livingspaces.values():
            database.database_insert_livingspace(room.name)
        for room in Amity.offices.values():
            database.database_insert_office(room.name)
        for person in Amity.fellows.values():
            database.database_insert_fellow(person.first_name,
                                            person.last_name,
                                            person.staff_id,
                                            person.allocated_office,
                                            person.allocated_livingspace)
        for person in Amity.staff.values():
            database.database_insert_staff(person.first_name,
                                            person.last_name,
                                            person.staff_id,
                                            person.allocated_office)
        return "Working data set saved to {} database".format(database_name)

    def load_state(database_name):
        """loads data from a specified database into the system"""

        #set the database to the specified database
        database = DatabaseConnections(database_name)
        for office in database.database_return_all_offices():
            Amity.create_room(office, "office")
        for livingspace in database.database_return_all_livingspaces():
            Amity.create_room(livingspace, "livingspace")
        for person in database.database_return_all_fellows():
            Amity.add_fellow_from_database(person[0], person[1], person[2], person[3],
                                            person[4])
        for person in database.database_return_all_staff():
            Amity.add_staff_from_database(person[0], person[1], person[2], person[3])

        return "\nDatabase {} has been loaded in the working data set\n".format(database_name)

    def load_people(filename):
        """loads people into the system from specified file"""
        
        print("Loading people from {} ...".format(filename))
        people = []
        with open("./datafiles/"+filename) as data:
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
