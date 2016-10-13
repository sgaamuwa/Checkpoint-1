import os.path
import unittest

from classes.amity import Amity
from classes.person import Fellow
from classes.person import Person
from classes.person import Staff
from unittest.mock import patch
from unittest.mock import PropertyMock

class AmityTest(unittest.TestCase):
    
    def setup(self):
        pass
       
    def test_object_of(self):
        obj = Amity()
        self.assertEqual(True, type(obj) is Amity)
    
    def test_create_room(self):
        #test that create room creates both offices and livingspaces
        #query the dictionaries to see the rooms are created
        self.assertEqual(len(Amity.offices), 0)
        Amity.create_room("Oculus", "office")
        self.assertEqual(len(Amity.offices), 1)
        self.assertIn("Oculus", Amity.offices.keys())
    
        self.assertEqual(len(Amity.livingspaces), 0)
        Amity.create_room("Python", "livingspace")
        self.assertEqual(len(Amity.livingspaces), 1)
        self.assertIn("Python", Amity.livingspaces.keys())
        
    @patch("builtins.input", lambda x : 'ST-01')
    def test_adds_person(self):
        #test that new people are actually assigned rooms
        with patch("classes.amity.Staff") as patched_staff:
            self.assertEqual(len(Amity.staff), 0)
            Amity.add_person("Samuel", "Gaamuwa", "STAFF")
            self.assertEqual(len(Amity.staff), 1)
        with patch("classes.amity.Fellow") as patched_fellow:
            self.assertEqual(len(Amity.fellows), 0)
            Amity.add_person("Samuel", "Gaamuwa", "FELLOW")
            self.assertEqual(len(Amity.fellows), 1)
    
    def test_assigns_livingspace(self):
        #test assigns room if requested
        Amity.create_room("Python", "livingspace")
        sam = Fellow("Samuel", "Gaamuwa", "ST-01")
        Amity.assign_livingspace(sam)
        self.assertEqual(sam.allocated_livingspace, "Python")

    
    def test_cant_assign_rooms_full(self):
        #test that new people cant be randomly assigned to full rooms
        #the save function in person automatically calls the assign room function 
        Amity.create_room("Oculus", "office")
        Amity.offices["Oculus"].current_occupants = ["Rehema Tadaa",
        "Ruth Tadaa", "Arnold Tadaa", "Whitney Tadaa", "Kimani Tadaa", "Migwi T"]
        sam = Staff("Samuel", "Gaamuwa", "ST-01")
        result = Amity.assign_room(sam)
        self.assertEqual("All current rooms are full", result)
    
    def test_reallocates_person(self):
        #tests that people are reallocated to requested rooms 
        Amity.create_room("Narnia", "office")
        sam = Staff("Samuel", "Gaamuwa", "ST-01")
        sam.allocated_office = "Narnia"
        Amity.offices["Narnia"].current_occupants.append("Samuel Gaamuwa")
        Amity.create_room("Valhala", "office")
        print(Amity.offices)
        Amity.reallocate(sam, "Valhala")
        self.assertNotIn("Samuel Gaamuwa", Amity.offices["Narnia"].current_occupants)
        self.assertIn("Samuel Gaamuwa", Amity.offices["Valhala"].current_occupants)
    
    def test_prints_allocations(self):
        #test it prints rooms and those allocated to them
        Amity.print_allocations("test_out.txt")
        self.assertTrue(os.path.isfile("../datafiles/test_out.text"))
    
    # def test_saves_state(self):
    #     #test that information can be stored in a new specified database
    #     Amity.save_state("new_database")
    #     self.assertTrue(os.path.isfile("../new_database"))
    
    # def test_loads_state(self):
    #     #test that it loads data from specified database
    #     Amity.load_state("new_rooms_db")
    #     self.assertIn("Valhala", Amity.print_allocations())
    #     self.assertIn("Hogwarts", Amity.print_allocations())

    # def test_loads_people(self):
    #     #test that it loads people from a specified file and allocates them rooms
    #     Amity.load_people("new_people")
    #     self.assertIn("Samuel Gaamuwa", Amity.print_allocations())
    #     self.assertIn("Isaac Dhibikirwa", Amity.print_allocations())

if __name__ == '__main__':
    unittest.main()
