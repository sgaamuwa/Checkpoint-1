import unittest


class Staff_Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = Staff()
        self.assertIsInstance(obj, Staff)
    
    def test_object_of(self):
        obj = Staff()
        self.assertEqual(True, type(obj) is Staff) 


if __name__ == '__main__':
    unittest.main()
