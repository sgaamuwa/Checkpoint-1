import os.path
import unittest


class AmityTest(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = Amity()
        self.assertIsInstance(obj, Amity)
    
    def test_object_of(self):
        obj = Amity()
        self.assertEqual(True, type(obj) is Amity)
    
    def test_create_room(self):
        #test that create room creates both offices and livingspaces
        #query the database to see the rooms are created 
        Amity.create_room("Oculus", "office")
        self.assertIsNotNone(database_return_office("Oculus"))
        Amity.create_room("Python", "living space")
        self.assertIsNotNone(database_return_livingspace("Python"))
    
    def test_assign_room(self):
        #test that new people are actually assigned rooms 
        Amity.create_room("Oculus", "office")
        sam = Staff("Samuel Gaamuwa", "09/09/2000", "Learning", "Sensei")
        Amity.assign_room(sam)
        self.assertIsNotNone(sam.allocated_office)
    
    def test_cant_assign_rooms_full(self):
        #test that new people cant be randomly assigned to full rooms
        #the save function in person automatically calls the assign room function 
        Amity.create_room("Oculus", "office")

        kimani = Fellow("Kimani Ndegu", "08/08/2001", 9, "D1")
        kimani.save()

        ruth = Fellow("Ruth Ogendi", "07/07/2001", 9, "D1")
        ruth.save()

        migwi = Fellow("Migwi N'dugu", "06/06/2001", 9, "D1")
        migwi.save()

        mark = Staff("Mark Kawanguzi", "05/05/2001", "Operations", "Tosan")
        mark.save()

        tim = Staff("Timothy Isiko", "04/04/2001", "Success", "Taichou")
        tim.save()

        martha = Staff("Martha Kyozira", "03/03/2001", "Technology", "Shinobi")
        martha.save()

        sam = Staff("Samuel Gaamuwa", "09/09/2000", "Learning", "Sensei")
        result = Amity.assign_room(sam)
        self.assertRaises("Can't assign room, all rooms full", result)
    
    def test_reallocates_person(self):
        #tests that people are reallocated to requested rooms 
        Amity.create_room("Narnia", "office")

        steve = Staff("Steve Njoro", "17/08/2000", "Success", "Facilitator")
        steve.save()

        Amity.create_room("Oculus", "office")
        Amity.reallocate(steve.name, "Oculus")
        self.assertEqual(steve.allocated_office, "Oculus")
    
    def test_prints_allocations(self):
        #test it prints rooms and those allocated to them
        Amity.create_room("Oculus", "office")

        sam = Staff("Samuel Gaamuwa", "09/09/2000", "Learning", "Sensei")

        Amity.assign_room(sam)
        self.assertIn("Oculus", Amity.print_allocations())
        self.assertIn("Samuel Gaamuwa", Amity.print_allocations())
    
    def test_saves_state(self):
        #test that information can be stored in a new specified database
        Amity.save_state("new_database")
        self.assertTrue(os.path.isfile("../new_database"))
    
    def test_loads_state(self):
        #test that it loads data from specified database
        Amity.load_state("new_rooms_db")
        self.assertIn("Valhala", Amity.print_allocations())
        self.assertIn("Hogwarts", Amity.print_allocations())

    def test_loads_people(self):
        #test that it loads people from a specified file and allocates them rooms
        Amity.load_people("new_people")
        self.assertIn("Samuel Gaamuwa", Amity.print_allocations())
        self.assertIn("Isaac Dhibikirwa", Amity.print_allocations())

if __name__ == '__main__':
    unittest.main()
