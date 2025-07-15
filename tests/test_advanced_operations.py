import pytest
from advanced_operations import power, sqrt, factorial
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