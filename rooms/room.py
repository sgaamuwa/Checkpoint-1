import os

from buildings.amity import Amity

class Room(object):

    def __init__(self, name, room_id):
        self.name = name
        self.room_id = room_id
        self.max_occupants = 6
        self.current_occupants = 0

    def search(name):
        for room in Amity.offices.values():
            if room.name = name:
                return "Room {} has {} occupants".format(name, room.current_occupants)
