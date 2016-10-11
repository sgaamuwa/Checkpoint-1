

class Room(object):

    def __init__(self, name):
        self.name = name
        self.max_occupants = 6
        self.current_occupants = []
