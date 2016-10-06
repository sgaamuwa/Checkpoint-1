import unittest

from people.staff import Staff


class StaffTest(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_object_of(self):
        obj = Staff("name")
        self.assertEqual(True, type(obj) is Staff) 


if __name__ == '__main__':
    unittest.main()
