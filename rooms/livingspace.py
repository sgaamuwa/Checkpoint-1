from rooms.room import Room


class LivingSpace(Room):
    def __init__(self, name):
        super().__init__(name)
        self.max_occupants = 4
