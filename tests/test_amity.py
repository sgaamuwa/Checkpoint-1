import unittest


class Amity_Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = Amity()
        self.assertIsInstance(obj, Amity)
    
    def test_object_of(self):
        obj = Amity()
        self.assertEqual(True, type(obj) is Amity)
    
    def test_create_room(self):
        Amity.create_room("Oculus", "office")
        self.assertEqual(Office.objects.count, 1)
        Amity.create_room("Python", "living space")
        self.assertEqual(LivingSpace.objects.count, 1)
    
    def test_assign_room(self):
        sam = Amity("Samuel Gaamuwa", "09/09/2000")
        sam.save()
        self.assertIsNotNone(sam.allocated_office)
    
    def test_cant_assign_rooms_full(self):
        sam = Amity("Samuel Gaamuwa", "09/09/2000")
        result = sam.save()
        self.assertRaises("Can't assign room, all rooms full", result)
    
    def test_reallocates_person(self):
        steve = Staff("Steve Njoro", "17/08/2000", "Success", "Facilitator")
        steve.save()
        Amity.reallocate(steve.name, "Oculus")
        self.assertEqual(steve.allocated_office, "Oculus")
    
    def test_prints_allocations(self):
        pass
    
    def test_saves_state(self):
        pass
    
    def test_loads_state(self):
        pass


if __name__ == '__main__':
    unittest.main()
