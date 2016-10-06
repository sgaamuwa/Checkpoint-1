import unittest

from rooms.room import Room
from people.staff import Staff
from people.fellow import Fellow
from buildings.amity import Amity


class RoomTest(unittest.TestCase):
    
    def setup(self):
        pass
        
    def test_object_of(self):
        obj = Room("name")
        self.assertEqual(True, type(obj) is Room)

    def test_can_search_room(self):
        #test that you can search for a room and its information
        Amity.create_room("Oculus", "office")
        result = Room.search("Oculus")
        self.assertIn("ROOM: Oculus\nTYPE: office", result)
    

if __name__ == '__main__':
    unittest.main()
