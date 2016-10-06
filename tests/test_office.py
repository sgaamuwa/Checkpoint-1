import unittest

from rooms.office import Office


class OfficeTest(unittest.TestCase):
    
    def setup(self):
        pass
        
    def test_object_of(self):
        obj = Office("name")
        self.assertEqual(True, type(obj) is Office)


if __name__ == '__main__':
    unittest.main()

