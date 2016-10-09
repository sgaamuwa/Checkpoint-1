import unittest

from buildings.amity import Amity
from people.fellow import Fellow
from people.person import Person
from people.staff import Staff
from database.database_connections import database_return_staff
from database.database_connections import database_return_fellow


class PersonTest(unittest.TestCase):

    def setup(self):
        pass
    
    def test_object_of(self):
        obj = Person("fname", "lname")
        self.assertEqual(True, type(obj) is Person) 
    
    def test_adds_person(self):
        #test that a person is added to the system and database
        sam = Staff("Samuel", "Gaamuwa")
        sam.save()
        isaac = Fellow("Isaac", "Dhibikirwa")
        isaac.save()
        self.assertIsNotNone(database_return_staff("Samuel", "Gaamuwa"))
        self.assertIsNotNone(database_return_fellow("Isaac", "Dhibikirwa"))
    
    def test_requests_reallocation(self):
        #test that a person can be reallocated to an office they request
        #the reallocation request calls the reallocation function in Amity
        Amity.create_room("Oculus", "office")

        sam = Staff("Samuel", "Gaamuwa")
        sam.save()

        Amity.create_room("Narnia", "office")

        Person.request_reallocation(sam.first_name, "Narnia")
        self.assertEqual(sam.allocated_office, "Narnia")
    
    def test_refuses_reallocation_to_full_office(self):
        #test that if a person requests reallocation to a full office it is denied
        #create office and assign six people to it  
        Amity.create_room("Valhala", "office")

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

        Amity.create_room("Narnia", "office")

        sam = Staff("Samuel", "Gaamuwa")
        #specify that sam is allocated to Narnia initially 
        sam.allocated_office = "Narnia"

        request = Person.request_reallocation(sam.first_name, "Valhala")
        self.assertEqual("Can't reallocate, room is full", request)
    
    def test_prints_unallocated(self):
        #test that the unallocated people are printed
        sam =  Staff("Samuel", "Gaamuwa")
        sam.save()
        result = Person.print_unallocated()
        self.assertIn("Samuel", "Gaamuwa", result)

if __name__ == '__main__':
    unittest.main()
