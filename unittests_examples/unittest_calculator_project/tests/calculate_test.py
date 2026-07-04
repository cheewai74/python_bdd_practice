import unittest
import sys

sys.path.insert(0, './src')

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """ 
        Test that adding two numbers returns the correct result.
        """
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        """ 
        Test that subtracting two numbers returns the correct result.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        """ 
        Test that multiplying two numbers returns the correct result.
        """
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide(self):
        """
        Test that dividing by a non-zero number returns the correct result.
        """
        self.assertEqual(self.calc.divide(5, 1), 5)

    def test_divide_by_zero(self):
        """
        Test that dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()