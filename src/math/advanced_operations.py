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