import os
import unittest

from classes.amity import Amity
from os import path
from unittest.mock import patch, PropertyMock, MagicMock, Mock


class AmityTest(unittest.TestCase):
       
    def test_object_of(self):
        obj = Amity()
        self.assertTrue(type(obj) is Amity)
    
    def test_create_room(self):
        #test that create room creates both offices and livingspaces
        #query the dictionaries to see the rooms are created
        with patch("classes.amity.Office") as patched_office:
            Amity.create_room("Oculus", "office")
            self.assertIn("Oculus", Amity.offices.keys())
        #do the same for livingspace
        with patch("classes.amity.LivingSpace") as patched_lspace:
            Amity.create_room("Python", "livingspace")
            self.assertIn("Python", Amity.livingspaces.keys())
        
    @patch("builtins.input", side_effect=["Samuel", "Gaamuwa", 'ST-01'])
    def test_adds_person(self, input):
        #test that new people are actually assigned rooms
        with patch("classes.amity.Staff") as patched_staff:
            self.assertEqual(len(Amity.staff), 0)
            Amity.add_person("Samuel", "Gaamuwa", "STAFF")
            self.assertEqual(len(Amity.staff), 1)
        with patch("classes.amity.Fellow") as patched_fellow:
            self.assertEqual(len(Amity.fellows), 0)
            Amity.add_person("Samuel", "Gaamuwa", "FELLOW")
            self.assertEqual(len(Amity.fellows), 1)
    
    def test_assigns_office(self):
        #test that the room can assign a room
        #create mock object of the staff member 
        mock_staff = Mock()
        mock_staff.first_name = "Samuel"
        mock_staff.last_name = "Gaamuwa"
        mock_staff.staff_id = "ST-01"
        mock_staff.allocated_office = ""
        with patch("classes.room.Office") as patched_office:
            Amity.create_room("Oculus", "office")
        self.assertEqual(mock_staff.allocated_office, "")
        Amity.assign_room(mock_staff)
        self.assertEqual(mock_staff.allocated_office, "Oculus")
    
    def test_assigns_livingspace(self):
        #test assigns room if requested
        #create mock object of the fellow
        mock_fellow = Mock()
        mock_fellow.first_name = "Samuel"
        mock_fellow.last_name = "Gaamuwa"
        mock_fellow.staff_id = "FL-01"
        mock_fellow.allocated_office = "Narnia"
        mock_fellow.allocated_livingspace = ""
        with patch("classes.room.LivingSpace") as patched_livingspace:
            Amity.create_room("Python", "livingspace")
        self.assertEqual(mock_fellow.allocated_livingspace, "")
        Amity.assign_livingspace(mock_fellow)
        self.assertEqual(mock_fellow.allocated_livingspace, "Python")
        #return a value that is accessible by a . something 

    @patch("builtins.input", side_effect=["Samuel", "Gaamuwa", 'ST-01'])
    def test_cant_assign_rooms_full(self, input):
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
        #mock the fellow object 
        mock_fellow = Mock()
        mock_fellow.first_name = "Samuel"
        mock_fellow.last_name = "Gaamuwa"
        mock_fellow.staff_id = "FL-01"
        mock_fellow.allocated_office = "Narnia"
        mock_fellow.allocated_livingspace = "Python"
        #mock the oculus office object and add to amity offices
        mock_office = Mock()
        mock_office.name = "Narnia"
        mock_office.current_occupants = ["Samuel Gaamuwa"]
        #add the mock object to the offices dictionary 
        Amity.offices["Narnia"] = mock_office
        with patch("classes.room.Office") as patched_office:
            Amity.create_room("Valhala", "office")
        self.assertEqual(mock_fellow.allocated_office, "Narnia")
        Amity.reallocate(mock_fellow, "Valhala")
        self.assertEqual(mock_fellow.allocated_office, "Valhala")
    
    def test_prints_allocations(self):
        #test it prints rooms and those allocated to them
        mock_office = Mock()
        mock_office.name = "Narnia"
        mock_office.current_occupants = ["Samuel Gaamuwa"]
        Amity.offices["Narnia"] = mock_office
        Amity.print_allocations("test_out.txt")
        self.assertTrue(path.isfile("./datafiles/test_out.txt"))
        with open("./datafiles/test_out.txt") as data:
            input = data.readlines()
            self.assertIn("Narnia(office)\n", input)
            self.assertIn("Samuel Gaamuwa, \n", input)

    def test_prints_unallocated(self):
        #test that it prints out unallocated to a test file
        Amity.print_unallocated("unallocated.txt")
        self.assertTrue(path.isfile("./datafiles/unallocated.txt"))
    
    @patch("classes.amity.DatabaseConnections")
    def test_saves_state(self, mock_db):
        mock_db.database_insert_livingspace.return_value = None
        mock_db.database_insert_office.return_value = None
        mock_db.database_insert_fellow.return_value = None
        mock_db.database_insert_staff.return_value = None
        #test that information can be stored in a new specified database
        Amity.save_state("new_database")
        self.assertTrue(os.path.isfile("./new_database"))

    @patch("classes.amity.DatabaseConnections")
    def test_loads_state(self, mock_data):
        #test that it loads data from specified database
        mock_data.database_return_all_offices.return_value = ["Hogwarts", "Narnia"]
        mock_data.database_return_all_livingspaces.return_value = ["Python", "Haskel"]
        mock_data.database_return_all_fellows.return_value = [("sam", "g", "1", "Hogwarts", "haskel")]
        mock_data.database_return_all_staff.return_value = [("rehema", "w", "2", "Hogwarts")]
        data = Amity.load_state("new_rooms_db")
        #assert confirmation of loading to system
        self.assertEqual("\nDatabase new_rooms_db has been loaded in the working data set\n", data)

    @patch("builtins.input", side_effect=["ST-01", "ST-02"])
    def test_loads_people(self, mock_input):
        #test that it loads people from a specified file and allocates them rooms
        #mock the office object
        mock_office = Mock()
        mock_office.name = "Narnia"
        mock_office.current_occupants = []
        Amity.offices["Narnia"] = mock_office
        #assert that the office occupants are none
        self.assertEqual(len(Amity.offices["Narnia"].current_occupants), 0)
        #load people into the system
        Amity.load_people("new_people.txt")
        #assert that the loaded people are in the system
        self.assertIn("ST-01 Samuel Gaamuwa", Amity.offices["Narnia"].current_occupants)
        self.assertIn("ST-02 Isaac Dhibikirwa", Amity.offices["Narnia"].current_occupants)

if __name__ == '__main__':
    unittest.main()
