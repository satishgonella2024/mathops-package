import unittest
import math

from advanced_math import AdvancedMath

class TestAdvancedMath(unittest.TestCase):

    def test_power(self):
        self.assertAlmostEqual(AdvancedMath.power(2, 3), 8)
        self.assertAlmostEqual(AdvancedMath.power(5, 2), 25)
        self.assertAlmostEqual(AdvancedMath.power(10, 0), 1)
        self.assertRaises(ValueError, AdvancedMath.power, -2, 0.5)

    def test_sqrt(self):
        self.assertAlmostEqual(AdvancedMath.sqrt(4), 2)
        self.assertAlmostEqual(AdvancedMath.sqrt(25), 5)
        self.assertAlmostEqual(AdvancedMath.sqrt(1), 1)
        self.assertRaises(ValueError, AdvancedMath.sqrt, -1)

    def test_factorial(self):
        self.assertEqual(AdvancedMath.factorial(0), 1)
        self.assertEqual(AdvancedMath.factorial(1), 1)
        self.assertEqual(AdvancedMath.factorial(5), 120)
        self.assertRaises(ValueError, AdvancedMath.factorial, -3)
        self.assertRaises(TypeError, AdvancedMath.factorial, 4.5)

if __name__ == '__main__':
    unittest.main()