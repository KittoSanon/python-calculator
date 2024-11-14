import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(95, 23), 118)
        self.assertEqual(self.calc.add(29, 83), 112)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 9), -4)
        self.assertEqual(self.calc.subtract(30, 55), -25)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(17, 28), 476)
        self.assertEqual(self.calc.multiply(97, 2), 194)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(86, 91), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(76, 59), 17)
        self.assertEqual(self.calc.modulo(59, 1), 0)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()