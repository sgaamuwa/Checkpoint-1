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
        pass
    def test_refuses_room(self):
        pass 

if __name__ == '__main__':
    unittest.main()
