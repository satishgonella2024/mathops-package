import math

class AdvancedMath:
    """
    A class for advanced mathematical operations.
    """

    @staticmethod
    def power(base, exponent):
        """
        Calculate the power of a base raised to an exponent.

        Args:
            base (float): The base value.
            exponent (float): The exponent value.

        Returns:
            float: The result of the power operation.

        Raises:
            ValueError: If the base is negative and the exponent is not an integer.
        """
        if base < 0 and exponent != int(exponent):
            raise ValueError("Base cannot be negative for non-integer exponents.")
        return base ** exponent

    @staticmethod
    def sqrt(number):
        """
        Calculate the square root of a number.

        Args:
            number (float): The number to calculate the square root of.

        Returns:
            float: The square root of the number.

        Raises:
            ValueError: If the number is negative.
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(number)

    @staticmethod
    def factorial(number):
        """
        Calculate the factorial of a number.

        Args:
            number (int): The number to calculate the factorial of.

        Returns:
            int: The factorial of the number.

        Raises:
            ValueError: If the number is negative.
            TypeError: If the number is not an integer.
        """
        if not isinstance(number, int):
            raise TypeError("Factorial is only defined for integers.")
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if number == 0:
            return 1
        return number * AdvancedMath.factorial(number - 1)