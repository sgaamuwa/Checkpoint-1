# AMITY ROOM ALLOCATION
The Amity Room Allocation application is a command line based application that randomly allocates users,
that is Staff and Fellows to Rooms in Amity. 
Fellows are automatically assigned living spaces, but can decide if they want to be allocated accommodation
spaces or not. Staff members are restricted to offices and can not be allocated accommodation.

##Dependencies
The Amity Room Allocation application implements/is built using the technologies and packages listed below:
* **[Python3](https://www.python.org/download/releases/3.0/)**
* **[SqlAlchemy](http://docs.sqlalchemy.org/en/latest/)**
* **[TermColor](https://pypi.python.org/pypi/termcolor)**
* **[PyFiglet](https://pypi.python.org/pypi/pyfiglet)**

The application is built solely in python with SqlAlchemy used for to create and query the database 

##Functions 
The application has the following functionality
* Creating rooms within amity. 
    * You can create multiple rooms of the same type after which you specify the kind of rooms that 
    you want to create.
    * Rooms created can either be livingspaces or offices.
* Adding people to the system.
    * People are added the system and specified as either fellows or staff members.
    * Fellows have the ability to request for livingspaces upon addition.
    * Fellows and Staff must all be given a staff member unique to them to be used in the system.
* Reallocating people to different rooms
    * The system can reallocate people using their staff numbers to a room of their choice, assuming the said room 
    is not full.
    * The offices have a maximum capacity of six and the livingspaces a maximum capacity of four.
* Printing the rooms and their allocations.
    * The system displays all people within the system and the rooms to which they have been allocated
    * The system also prints out the allocations to a file if it is specified.
* Printing unallocated persons
    * Just as with printing rooms and allocations, the system can print people that are not allocated to rooms but
    are in the system
* Saving the state of the system to a database
    * The system works with a volatile data set, till it is persisted to a database, this is done using the save 
    state command 
* Loading state from a database
    * Information can be loaded into the working data set of the system from a database by specifying the database 
    to be used. 
* Loading from a text file
    * Just like the load state, people can be loaded into the system from a text file if it follows the format below:
           
            OLUWAFEMI SULE FELLOW Y
            DOMINIC WALTERS STAFF
            SIMON PATTERSON FELLOW Y
            MARI LAWRENCE FELLOW Y
            LEIGH RILEY STAFF
            TANA LOPEZ FELLOW Y
            KELLY McGUIRE STAFF
            

###Command doc 
* This is the command document for the application 
            
            Usage:
                create_room <room_name>...
                add_person <first_name> <last_name> <title> [--wa=N]
                reallocate_person <person_identifier> <new_room_name>
                load_people <filename>
                print_room <room_name>
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
            