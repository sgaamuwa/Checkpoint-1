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
        sam = Person("Samuel Gaamuwa", "09/09/2000")
        sam.save()
        #assert Samuel Gaamuwa is in database
    def test_requests_reallocation(self):
        pass
    def test_prints_unallocated(self):
        Person.print_unallocated()
        #assert the contents of the print

if __name__ == '__main__':
    unittest.main()
