import unittest

from buildings.amity import Amity
from people.fellow import Fellow
from people.person import Person
from people.staff import Staff
from database.database_connections import database_return_staff
from database.database_connections import database_return_fellow


class PersonTest(unittest.TestCase):

    def setup(self):
        pass
    
    def test_object_of(self):
        obj = Person("name")
        self.assertEqual(True, type(obj) is Person) 

if __name__ == '__main__':
    unittest.main()
