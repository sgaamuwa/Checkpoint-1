import unittest

class Office_Test(unittest.TestCase):
    def setup(self):
        pass
    def test_instance_of(self):
        obj = Office()
        self.assertIsInstance(obj, Office)
    def test_object_of(self):
        obj = Office()
        self.assertEqual(True, type(obj) is Office)

if __name__ == '__main__':
    unittest.main()

