import os


class Room(object):

    def __init__(self, name, room_id):
        self.name = name
        self.room_id = room_id
        self.max_occupants = 6
        self.current_occupants = 0
