# tests/test_calculator.py

import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()