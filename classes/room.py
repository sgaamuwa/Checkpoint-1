

class Room(object):

    def __init__(self, name):
        self.name = name
        self.max_occupants = 6
        self.current_occupants = []

    def print_room(self):
        """prints all the current occupants of the room"""

        print(self.name + "\n")
        print("-"*80)
        print("\n")
        for person in self.current_occupants:
            print(person + ", ", end=" ")


class Office(Room):
    pass

   
class LivingSpace(Room):
    def __init__(self, name):
        super().__init__(name)
        self.max_occupants = 4
