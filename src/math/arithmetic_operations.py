class ArithmeticOperations:
    """
    A class to perform basic arithmetic operations.
    """

    @staticmethod
    def add(a, b):
        """
        Add two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of the two numbers.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Subtract two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The difference between the two numbers.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divide two numbers.

        Args:
            a (int or float): The dividend.
            b (int or float): The divisor.

        Raises:
            ZeroDivisionError: If the divisor is zero.

        Returns:
            int or float: The quotient of the two numbers.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b