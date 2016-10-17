import sys
import unittest

from classes.room import Room


class RoomTest(unittest.TestCase):
        
    def test_object_of(self):
        obj = Room("name")
        self.assertEqual(True, type(obj) is Room)

    def test_print_room(self):
        #test can print occupants of the room 
        oculus = Room("Oculus")
        oculus.current_occupants.append("Samuel Gaamuwa")
        result = oculus.print_room()
        self.assertEqual("Room Oculus printed", result)

if __name__ == '__main__':
    unittest.main()
