class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 2), 5)
""")

with open('math_operations/tests/test_advanced.py', 'w') as f:
    f.write("""
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
""")

This code creates the following Python package structure:

math_operations/
├── __init__.py
├── basic/
│   ├── __init__.py
│   └── arithmetic.py
├── advanced/
│   ├── __init__.py
│   └── advanced.py
└── tests/
    ├── __init__.py
    ├── test_arithmetic.py
    └── test_advanced.py

The package includes the following modules:
- `math_operations.basic.arithmetic`: Provides basic arithmetic operations (add, subtract, multiply, divide)
- `math_operations.advanced.advanced`: Provides advanced mathematical operations (power, square root, factorial)
- `math_operations.tests.test_arithmetic`: Unit tests for the basic arithmetic operations
- `math_operations.tests.test_advanced`: Unit tests for the advanced mathematical operations

The package structure follows the standard Python package layout, with the necessary `__init__.py` files to make the package importable. You can now use this package structure to implement the required mathematical operations and their corresponding unit tests.