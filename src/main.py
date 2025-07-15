Here is the Python package structure with the necessary directories and __init__.py files:

import os

# Create the package directory structure
os.makedirs('math_operations/basic', exist_ok=True)
os.makedirs('math_operations/advanced', exist_ok=True)
os.makedirs('math_operations/tests', exist_ok=True)

# Create the __init__.py files
open('math_operations/__init__.py', 'w').close()
open('math_operations/basic/__init__.py', 'w').close()
open('math_operations/advanced/__init__.py', 'w').close()
open('math_operations/tests/__init__.py', 'w').close()

# Create the main module files
with open('math_operations/basic/arithmetic.py', 'w') as f:
    f.write("""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
""")

with open('math_operations/advanced/advanced.py', 'w') as f:
    f.write("""
import math

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def factorial(n):
    return math.factorial(n)
""")

with open('math_operations/tests/test_arithmetic.py', 'w') as f:
    f.write("""
import unittest
from math_operations.basic.arithmetic import add, subtract, multiply, divide