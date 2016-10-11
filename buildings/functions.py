import os 

from buildings.amity import Amity

def request_reallocation(staff_id, room):
    """parses the object of the staff_id to amity for reallocation"""
    
    if staff_id in Amity.staff.keys():
        person = Amity.reallocate(Amity.staff[staff_id], room)
        Amity.staff[staff_id] = person
    elif staff_id in Amity.fellows.keys():
        person = Amity.reallocate(Amity.fellows[staff_id], room)
        Amity.fellows[staff_id] = person

def create_room(*args):
    """sorts through the input rooms and creates each room"""
    if "office" in args:
        for room in args:
            if room != "office":
                Amity.create_room(room, "office")
    elif "livingspace" in args:
        for room in args:
            if room != "livingspace":
                Amity.create_room(room, "livingspace")

create_room("Oculus", "Narnia", "Krypton", "office")
Amity.print_allocations("output.txt")