import unittest

from classes.person import Person


class PersonTest(unittest.TestCase):

    def test_object_of(self):
        obj = Person("first", "last", "SD-ID")
        self.assertTrue(type(obj) is Person) 

if __name__ == '__main__':
    unittest.main()
