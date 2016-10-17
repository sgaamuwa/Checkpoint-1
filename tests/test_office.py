import unittest

from classes.room import Office


class OfficeTest(unittest.TestCase):
    
    def test_object_of(self):
        obj = Office("name")
        self.assertEqual(True, type(obj) is Office)


if __name__ == '__main__':
    unittest.main()

