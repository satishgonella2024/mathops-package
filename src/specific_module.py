"""
math_operations.py
This module provides basic and advanced mathematical operations.
"""

import math
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts two numbers.

    Args:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The difference between the two numbers.
    """
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number to multiply.
        b (int or float): The second number to multiply.

    Returns:
        int or float: The product of the two numbers.
    """
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divides two numbers.

    Args:
        a (int or float): The number to divide.
        b (int or float): The number to divide by.

    Returns:
        int or float: The quotient of the two numbers.

    Raises:
        ZeroDivisionError: If the second argument is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Raises a number to a power.

    Args:
        base (int or float): The base number.
        exponent (int or float): The exponent.

    Returns:
        int or float: The result of raising the base to the exponent.
    """
    return base ** exponent

def sqrt(a: Union[int, float]) -> float:
    """
    Calculates the square root of a number.

    Args:
        a (int or float): The number to find the square root of.

    Returns:
        float: The square root of the number.

    Raises:
        ValueError: If the number is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)

def factorial(n: int) -> int:
    """
    Calculates the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If the number is negative.
    """
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    return math.factorial(n)