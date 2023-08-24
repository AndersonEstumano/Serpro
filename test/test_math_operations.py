import unittest 
from math_operations import add, sub, mul, div

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(2, 0), 2)
    
    def test_sub(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(2, -3), 5)
        self.assertEqual(sub(-2, -3), 1)
        self.assertEqual(sub(2, 0), 2)
    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(2, -3), -6)
        self.assertEqual(mul(-2, -3), 6)
        self.assertEqual(mul(2, 0), 0)
    def test_div(self):
        self.assertEqual(div(2, 3), 2/3)
        self.assertEqual(div(2, -3), 2/-3)
        self.assertEqual(div(-2, -3), -2/-3)

        
if __name__ == '__main__':
    unittest.main()