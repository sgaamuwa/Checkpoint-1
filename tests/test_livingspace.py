import unittest


class LivingSpace_Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_object_of(self):
        obj = LivingSpace("name")
        self.assertEqual(True, type(obj) is LivingSpace)

if __name__ == '__main__':
    unittest.main()
