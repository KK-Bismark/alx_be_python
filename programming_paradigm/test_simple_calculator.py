# A unittest for the simple calculator implementation.


import unittest
from simple_calculator import SimpleCalculator


class SimpleCalculatorTest(unittest.TestCase):

    def setUp(self):
        """ Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # test case for addition
    def test_addition(self):
        """ Test for addition."""
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(2, -1), 1)
        self.assertEqual(self.calc.add(2, 0), 2)

    # test case for subtraction
    def test_subtraction(self):
        """Test for subtraction."""
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(1, 0), 1)
        self.assertEqual(self.calc.subtract(1, -1), 2)

    # test case for multiplication
    def test_multiply(self):
        """Test for multiplication."""
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(11, 1), 11)

    # test case for division function
    def test_divide(self):
        """Test for division."""
        self.assertEqual(self.calc.divide(2, 0), ZeroDivisionError)
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(0, 2), 0)
