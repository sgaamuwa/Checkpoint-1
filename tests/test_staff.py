import unittest

from classes.person import Staff


class StaffTest(unittest.TestCase):
    
    def test_object_of(self):
        obj = Staff("Samuel", "Gaamuwa", "ST-01")
        self.assertEqual(True, type(obj) is Staff) 


if __name__ == '__main__':
    unittest.main()
