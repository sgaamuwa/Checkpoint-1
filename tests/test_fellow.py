import unittest


class Fellow_Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = Fellow()
        self.assertIsInstance(obj, Fellow) 
    
    def test_object_of(self):
        obj = Fellow()
        self.assertEqual(True, type(obj) is Fellow) 
    
    def test_requests_livingspace(self):
        kimani = Fellow("Kimani Kim", "09/08/2000", 9, "D1")
        kimani.request_livingspace()
        self.assertIsNotNone(kimani.allocated_livingspace)


if __name__ == '__main__':
    unittest.main()
