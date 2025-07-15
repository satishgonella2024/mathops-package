import unittest
from math_operations.advanced.advanced import power, sqrt, factorial

class TestAdvanced(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(0, 0), 1)

    def test_sqrt(self):
        self.assertAlmostEqual(sqrt(16), 4.0)
        self.assertAlmostEqual(sqrt(2), 1.4142135623730951)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)