from decimal import Decimal
import numbers
import re

class Calculator:
    NUMBER_PATTERN = r"^[-+]?\d*\.?\d+$"

    @classmethod
    def _parse_and_validate(cls, num):
        """Helper method to parse and validate a number."""
        if isinstance(num, str):
            if not re.match(cls.NUMBER_PATTERN, num):
                # Using a custom error for better clarity on type mismatch
                raise TypeError(f"'{num}' is not a valid number string.")
            return float(num)
        if isinstance(num, (int, float, Decimal)):
            return num
        # Catch all other non-numeric types
        raise TypeError(f"'{num}' is not a valid number type.")

    @classmethod
    def add(cls, num1, num2):
        num1 = cls._parse_and_validate(num1)
        num2 = cls._parse_and_validate(num2)
        return num1 + num2

    @classmethod
    def subtract(cls, num1, num2):
        num1 = cls._parse_and_validate(num1)
        num2 = cls._parse_and_validate(num2)
        return num1 - num2

    @classmethod
    def multiply(cls, num1, num2):
        num1 = cls._parse_and_validate(num1)
        num2 = cls._parse_and_validate(num2)
        return num1 * num2

    @classmethod
    def divide(cls, num1, num2):
        num1 = cls._parse_and_validate(num1)
        num2 = cls._parse_and_validate(num2)
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2