import pytest
from arithmetic_operations import ArithmeticOperations

class TestArithmeticOperations:
    def test_add(self):
        assert ArithmeticOperations.add(2, 3) == 5
        assert ArithmeticOperations.add(-1, 1) == 0
        assert ArithmeticOperations.add(2.5, 3.7) == 6.2

    def test_subtract(self):
        assert ArithmeticOperations.subtract(5, 3) == 2
        assert ArithmeticOperations.subtract(1, 1) == 0
        assert ArithmeticOperations.subtract(4.2, 1.7) == 2.5

    def test_multiply(self):
        assert ArithmeticOperations.multiply(2, 3) == 6
        assert ArithmeticOperations.multiply(-1, 1) == -1
        assert ArithmeticOperations.multiply(2.5, 3.7) == 9.25

    def test_divide(self):
        assert ArithmeticOperations.divide(6, 3) == 2
        assert ArithmeticOperations.divide(1, 1) == 1
        assert ArithmeticOperations.divide(4.2, 1.5) == 2.8

        with pytest.raises(ZeroDivisionError):
            ArithmeticOperations.divide(1, 0)