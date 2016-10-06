import os.path
import unittest

from buildings.amity import Amity
from people.fellow import Fellow
from people.person import Person
from people.staff import Staff
from database.database_connections import database_return_office
from database.database_connections import database_return_livingspace

class AmityTest(unittest.TestCase):
    
    def setup(self):
        pass
       
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
        sam = Staff("Samuel", "Gaamuwa")
        Amity.assign_room(sam)
        self.assertIsNotNone(sam.allocated_office)
    
    def test_cant_assign_rooms_full(self):
        #test that new people cant be randomly assigned to full rooms
        #the save function in person automatically calls the assign room function 
        Amity.create_room("Oculus", "office")

        kimani = Fellow("Kimani", "Ndegu")
        kimani.save()

        ruth = Fellow("Ruth", "Ogendi")
        ruth.save()

        migwi = Fellow("Migwi", "N'dugu")
        migwi.save()

        mark = Staff("Mark", "Kawanguzi")
        mark.save()

        tim = Staff("Timothy", "Isiko")
        tim.save()

        martha = Staff("Martha", "Kyozira")
        martha.save()

        sam = Staff("Samue", "Gaamuwa")
        result = Amity.assign_room(sam)
        self.assertEqual("Can't assign room, all rooms full", result)
    
    def test_reallocates_person(self):
        #tests that people are reallocated to requested rooms 
        Amity.create_room("Narnia", "office")

        steve = Staff("Steve", "Njoro")
        steve.save()

        Amity.create_room("Oculus", "office")
        Amity.reallocate(steve, "Oculus")
        self.assertEqual(steve.allocated_office, "Oculus")
    
    def test_refuses_reallocation_to_non_existent_office(self):
        #tests it does not allocate to non existent room
        Amity.create_room("Oculus", "office")

        sam = Staff("Samuel", "Gaamuwa")
        sam.save()

        request = Amity.reallocate(sam, "Narnia")
        self.assertEqual("Room Narnia does not exist", result)
    
    def test_prints_allocations(self):
        #test it prints rooms and those allocated to them
        Amity.create_room("Oculus", "office")

        sam = Staff("Samuel", "Gaamuwa")

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
