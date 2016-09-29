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
        Amity.create_room("Oculus", "office")
        result = Room.search("Oculus")
        self.assertIn("ROOM: Oculus\nTYPE: office", result)

    def test_prints_allocations(self):
        Amity.create_room("Oculus", "office")
        sam = Staff("Samuel Gaamuwa", "09/09/2000", "Learning", "Associate")
        kimani = Fellow("Kimani Ndegu", "08/08/2000", 9, "D1")
        arnold = Fellow("Arnold Okoth", "07/07/2000", 9, "D1")
        self.assertIn("Oculus", Room.print_allocations)
        self.assertIn("Samuel Gaamuwa", Room.print_allocations)
    

if __name__ == '__main__':
    unittest.main()
