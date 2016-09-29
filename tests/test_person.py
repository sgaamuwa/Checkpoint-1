import unittest


class Person_Test(unittest.TestCase):

    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = Person("name", "01/01/2016")
        self.assertIsInstance(obj, Person)
    
    def test_object_of(self):
        obj = Person("name", "01/01/2016")
        self.assertEqual(True, type(obj) is Person) 
    
    def test_adds_person(self):
        sam = Staff("Samuel Gaamuwa", "09/09/2000", "Facilities", "Coordinator")
        sam.save()
        result = Person.search("Samuel")
        self.assertIn("Samuel Gaamuwa", result)
    
    def test_requests_reallocation(self):
        sam = Staff("Samuel Gaamuwa", "09/09/2000", "Facilities", "Coordinator")
        sam.save()
        Person.request_reallocation(sam.name, "Narnia")
        self.assertEqual(sam.allocated_office, "Narnia")
    
    def test_refuses_reallocation_to_full_office(self):
        sam = Person("Samuel Gaamuwa", "09/09/2000")
        sam.save()
        #populate valhala with people
        request = Person.request_reallocation(sam.name, "Valhala")
        self.assertRaises("Can't reallocate, room is full", request)
    
    def test_prints_unallocated(self):
        Person.print_unallocated()
        #assert the contents of the print

if __name__ == '__main__':
    unittest.main()
