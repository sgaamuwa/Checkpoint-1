import unittest

from classes.room import LivingSpace


class LivingSpaceTest(unittest.TestCase):
    
    def test_object_of(self):
        obj = LivingSpace("name")
        self.assertTrue(type(obj) is LivingSpace)
        

if __name__ == '__main__':
    unittest.main()
