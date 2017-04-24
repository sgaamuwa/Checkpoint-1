

class Room(object):
    """Room class
    
    Defines the generic room in the system
    """

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
            print(person + ", ")

        return "Room {} printed".format(self.name)


class Office(Room):
    """Office class
    
    Inherits from the room class and defines offices as 
    specific rooms
    """
    def __init__(self, name):
        super().__init__(name)

   
class LivingSpace(Room):
    """LivingSpace class
    
    Inherits from the room class and defines livingspaces as 
    specific rooms
    """
    def __init__(self, name):
        super().__init__(name)
        self.max_occupants = 4
