import os.path
#import .path only 
import unittest

from classes.amity import Amity
from classes.person import Person
from unittest.mock import patch
from unittest.mock import PropertyMock, MagicMock
#merge these lines above

class AmityTest(unittest.TestCase):
    
    def setup(self):
        pass
       
    def test_object_of(self):
        obj = Amity()
        self.assertEqual(True, type(obj) is Amity)
        #use assert True
    
    def test_create_room(self):
        #test that create room creates both offices and livingspaces
        #query the dictionaries to see the rooms are created
        self.assertEqual(len(Amity.offices), 0)
        Amity.create_room("Oculus", "office")
        self.assertEqual(len(Amity.offices), 1)
        self.assertIn("Oculus", Amity.offices.keys())
        #you should have a patch here

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
    
    @patch("classes.room.LivingSpace")
    @patch("classes.person.Fellow")
    def test_assigns_livingspace(self, mock_fellow, mock_lspace):
        #test assigns room if requested
        mock_fellow.return_value = MagicMock(first_name="Samuel", last_name="Gaamuwa",
        staff_id="ST-01", allocated_office="Narnia", allocated_livingspace="")
        mock_lspace.return_value = MagicMock(name="Python", current_occupants=[])
        with patch("classes.room.LivingSpace") as patched_office:
            Amity.create_room("Python", "livingspace")
        Amity.assign_livingspace(mock_fellow)
        self.assertEqual(len(Amity.livingspaces["Python"].current_occupants), 1)
        #return a value that is accessible by a . something 

    @patch("builtins.input", lambda x : 'ST-01')
    def test_cant_assign_rooms_full(self):
        #test that new people cant be randomly assigned to full rooms
        #the save function in person automatically calls the assign room function
        with patch("classes.room.Office") as patched_office: 
            Amity.create_room("Oculus", "office")
            with patch("classes.person.Staff") as patched_staff:
                Amity.offices["Oculus"].current_occupants = ["Rehema Tadaa",
                "Ruth Tadaa", "Arnold Tadaa", "Whitney Tadaa", "Kimani Tadaa", "Migwi T"]
                result = Amity.add_person("Samuel", "Gaamuwa", "STAFF")
                self.assertEqual("Samuel Gaamuwa added but not assigned room", result)
    
    @patch("classes.room.Office")
    @patch("classes.person.Fellow")
    def test_reallocates_person(self, mock_fellow, mock_office):
        #tests that people are reallocated to requested rooms 
        mock_fellow.return_value = MagicMock(first_name="Samuel", last_name="Gaamuwa",
        staff_id="ST-01", allocated_office="Narnia")
        # mock_office.return_value = MagicMock(name="Oculus", current_occupants=[])
        with patch("classes.amity.Office") as patched_office:
            Amity.create_room("Oculus", "office")
        Amity.reallocate(mock_fellow, "Oculus")
        self.assertEqual(len(mock_office.current_occupants), 1)
    
    # def test_prints_allocations(self):
    #     #test it prints rooms and those allocated to them
    #     Amity.print_allocations("test_out.txt")
    #     self.assertTrue(os.path.isfile("../datafiles/test_out.text"))
    
    def test_saves_state(self):
        #test that information can be stored in a new specified database
        Amity.save_state("new_database")
        self.assertTrue(os.path.isfile("./new_database"))
    
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
