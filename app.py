"""
The Amity Room Allocation application is a system for assigning rooms
to staff and fellows. Rooms are assigned randomly when people are added
to the system.

Usage:
    create_room <room_name>...
    add_person <first_name> <last_name> <title> [--wa=N]
    reallocate_person <person_identifier> <new_room_name>
    load_people <filename>
    print_all_rooms
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db <sqlite_database>]
    load_state <sqlite_database>
    quit

Options:
    -h, --help  Show this screen and exit
    --o Output into a specified file
    --db Specify a database path
    --wa Specify wants accommodation 
"""


import cmd
import os 

from classes.amity import Amity
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def startup():
    cprint(figlet_format("AMITY ROOM", font="starwars"),
       "yellow", attrs=["bold"])

class AmityRoomAllocations(cmd.Cmd):
    prompt = "Amity&>>>"

    @docopt_cmd
    def do_create_room(self, args):
        """
        Creates new rooms in Amity
        Mulitple rooms of the same kind can be created at once
        The rooms are added to the command the room type added at the end

        Usage: create_room <room_name>...
        """
        rooms = args["<room_name>"]

        if "office" in rooms:
            for room in rooms:
                if room != "office":
                    Amity.create_room(room, "office")
        elif "livingspace" in rooms:
            for room in rooms:
                if room != "livingspace":
                    Amity.create_room(room, "livingspace")

    @docopt_cmd
    def do_add_person(self, args):
        """
        Adds a person to the System 
        One specified person is added to the system using their details
        First name, last name, type of employee
        For Fellows, they have the option to request for accommodation

        Usage: add_person <first_name> <last_name> <title> [--wa] 
        """
        print(args)
        Amity.add_person(args["<first_name>"], args["<last_name>"], args["<title>"],
                        args["[--wa]"])

    @docopt_cmd
    def do_reallocate_person(self, args):
        """
        Reallocates a person to a new room using their unique identifier
        When loaded into the system, each person has a unique staff_id number
        This is used to reallocate them to specific rooms

        Usage: reallocate_person <person_identifier> <new_room_name>
        """
        person = args["<person_identifier>"]
        room = args["<new_room_name>"]

        if person in Amity.fellows.keys():
            Amity.reallocate(Amity.fellows[person], room)
        elif person in Amity.staff.keys():
            Amity.reallocate(Amity.staff[person], room)

    @docopt_cmd
    def do_load_people(self, args):
        """
        Loads new people into the system from a specified text file in the format

        OLUWAFEMI SULE FELLOW Y
        DOMINIC WALTERS STAFF
        SIMON PATTERSON FELLOW Y
        MARI LAWRENCE FELLOW Y
        LEIGH RILEY STAFF
        TANA LOPEZ FELLOW Y
        KELLY McGUIRE STAFF

        The file is placed in the datafiles folder

        Usage: load_people <filename>
        """
        Amity.load_people(args["<filename>"])

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        Prints all the rooms in the system and the people allocated to them
        Also writes out the allocations to a text file if specified

        Usage: print_allocations [--o=filename]
        """
        if args["--o"] is None:
            print(Amity.print_allocations())
        else:
            Amity.print_allocations(args["--o"])

    @docopt_cmd
    def do_print_unallocated(self, args):
        """
        Prints out all the unallocated people in the System 
        Also writes out the unallocated people to a text file if specified 

        Usage: print_unallocated [--o=filename]
        """
        if args["--o"] is None:
            Amity.print_unallocated()
        else:
            Amity.print_unallocated(args["--o"])

    @docopt_cmd
    def do_print_room(self, args):
        """
        Prints out a single specified room and the people allocated to iter
        
        Usage: print_room <room_name>
        """
        room = args["<room_name>"]

        if room in Amity.offices.keys():
            Amity.offices[room].print_room()
        elif room in Amity.livingspaces.keys():
            Amity.livingspaces[room].print_room()
        else:
            print("Room does not exist")

    @docopt_cmd
    def do_save_state(self, args):
        """
        Persists all data in the system's working set to a specified database
        If no database is specified, a default amity_db is used

        Usage: save_state [--db=sqlite_database]
        """
        Amity.save_state(args["--db"])

    @docopt_cmd
    def do_load_state(self, args):
        """
        Loads data from a specified database into the system's working data set

        Usage: load_state <sqlite_database>
        """
        Amity.load_state(args["<sqlite_database>"])

    @docopt_cmd
    def do_quit(self, args):
        """
        Quits the application and automatically saves the session to the database

        Usage: quit
        """
        print("Any unsaved work will be lost\n")
        print("Are you sure you want to quit?\n")
        answer = input("Enter Yes or No: ").strip()
        if answer == "Yes":
            exit()
        elif answer == "No":
            pass 

if __name__ == "__main__":
    startup()
    AmityRoomAllocations().cmdloop()