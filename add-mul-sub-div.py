class Addition:
    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b


class Subtraction:
    @staticmethod
    def subtract(a, b):
        """Returns the difference between two numbers."""
        return a - b


class Multiplication:
    @staticmethod
    def multiply(a, b):
        """Returns the product of two numbers."""
        return a * b


class Division:
    @staticmethod
    def divide(a, b):
        """Returns the quotient of two numbers. Raises an exception if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example usage 
print(Addition.add(5, 3))
print(Subtraction.subtract(5, 3))
print(Multiplication.multiply(5, 3))
print(Division.divide(5, 3))
