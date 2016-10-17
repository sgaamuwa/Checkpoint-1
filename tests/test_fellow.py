import unittest

from classes.person import Fellow


class FellowTest(unittest.TestCase):
    
    def test_object_of(self):
        obj = Fellow("Samuel", "Gaamuwa", "FL-01")
        self.assertTrue(type(obj) is Fellow) 
    

if __name__ == '__main__':
    unittest.main()
