import unittest

from people.fellow import Fellow

class FellowTest(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_object_of(self):
        obj = Fellow("fname", "lname")
        self.assertEqual(True, type(obj) is Fellow) 
    
    def test_requests_livingspace(self):
        #tests that a fellow can request for a living space
        #the living space is then randomly assigned
        kimani = Fellow("Kimani", "Kim")
        kimani.request_livingspace()
        self.assertIsNotNone(kimani.allocated_livingspace)


if __name__ == '__main__':
    unittest.main()
