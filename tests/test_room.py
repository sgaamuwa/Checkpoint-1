import unittest


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

    def test_prints_allocations(self):
        Amity.create_room("Oculus", "office")
        sam = Staff("Samuel Gaamuwa")
        kimani = Fellow("Kimani Ndegu")
        arnold = Fellow("Arnold Okoth")
        self.assertIn("Oculus", Room.print_allocations())
        self.assertIn("Samuel Gaamuwa", Room.print_allocations())
    

if __name__ == '__main__':
    unittest.main()
