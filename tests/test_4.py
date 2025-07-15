{
    "code": "\
import math

def power(base, exponent):
    try:
        return base ** exponent
    except (ValueError, TypeError):
        raise ValueError('Invalid input for power function')

def sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        raise ValueError('Input must be a non-negative number')

def factorial(n):
    try:
        if n < 0:
            raise ValueError('Input must be a non-negative integer')
        elif n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    except (ValueError, TypeError):
        raise ValueError('Input must be a non-negative integer')
",
    "tests": "\
import pytest
from math import isnan

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 4) == 16
    with pytest.raises(ValueError):
        power('a', 2)
    with pytest.raises(ValueError):
        power(2, 'b')

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(1) == 1
    assert isnan(sqrt(-1))
    with pytest.raises(ValueError):
        sqrt(-2)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial('a')
",
    "documentation": "This module contains three functions for advanced mathematical operations: power, sqrt, and factorial. The power function calculates the result of raising a base to a given exponent. The sqrt function calculates the square root of a given number. The factorial function calculates the factorial of a given non-negative integer. All functions include input validation and raise appropriate exceptions for invalid inputs.",
    "dependencies": ["math"]
}