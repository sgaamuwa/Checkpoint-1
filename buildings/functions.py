import os 

from buildings.amity import Amity

def request_reallocation(staff_id, room):
    if staff_id in Amity.staff.keys():
        person = Amity.reallocate(Amity.staff[staff_id], room)
        Amity.staff[staff_id] = person
    elif staff_id in Amity.fellows.keys():
        person = Amity.reallocate(Amity.fellows[staff_id], room)
        Amity.fellows[staff_id] = person

def search(name):
    for room in Amity.offices.values():
        if room.name == name:
            result = room
            break
    for room in Amity.livingspaces.values():
        if room.name == name:
            result = room
            break
     return result