import unittest


class Room_Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = Room()
        self.assertIsInstance(obj, Room)
    
    def test_object_of(self):
        obj = Room()
        self.assertEqual(True, type(obj) is Room)

    def test_can_search_room(self):
        #test that you can search for a room and its information
        Amity.create_room("Oculus", "office")
        result = Room.search("Oculus")
        self.assertIn("ROOM: Oculus\nTYPE: office", result)


if __name__ == '__main__':
    unittest.main()
