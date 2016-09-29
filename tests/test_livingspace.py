import unittest


class LivingSpace_Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test_instance_of(self):
        obj = LivingSpace()
        self.assertIsInstance(obj, LivingSpace)
    
    def test_object_of(self):
        obj = LivingSpace()
        self.assertEqual(True, type(obj) is LivingSpace)

if __name__ == '__main__':
    unittest.main()
