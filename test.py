import unittest

from main import sort

class TestSortPackage(unittest.TestCase):
    def test_special_packages(self):
        self.assertEqual(sort(100,100,100,10), "SPECIAL")

        self.assertEqual(sort(100,10,150,19), "SPECIAL")
        self.assertEqual(sort(100,150,10,10), "SPECIAL")
        self.assertEqual(sort(150,10,100,10), "SPECIAL")
        
        self.assertEqual(sort(100,10,10,20), "SPECIAL")

        
    def test_heavy_packages(self):       
        self.assertEqual(sort(100,100,100,20), "HEAVY")

        self.assertEqual(sort(100,10,150,20), "HEAVY")
        self.assertEqual(sort(100,150,10,20), "HEAVY")
        self.assertEqual(sort(150,10,100,20), "HEAVY")


    def test_standard_packages(self):
        self.assertEqual(sort(100,10,100,19), "STANDARD")

        
    def test_zero_values_errors(self):
        with self.assertRaises(ValueError) as context:
            sort(0,10,10,10)
        self.assertEqual(str(context.exception), "Values must be greater than 0")
        
        with self.assertRaises(ValueError) as context:
            sort(10,0,10,10)
        self.assertEqual(str(context.exception), "Values must be greater than 0")
        
        with self.assertRaises(ValueError) as context:
            sort(10,10,-10,10)
        self.assertEqual(str(context.exception), "Values must be greater than 0")
        
        with self.assertRaises(ValueError) as context:
            sort(10,10,10,0)
        self.assertEqual(str(context.exception), "Values must be greater than 0")

        
if __name__ == '__main__':
    unittest.main()