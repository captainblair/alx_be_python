#!/usr/bin/env python3
"""
Demonstrates the difference between @staticmethod and @classmethod using a Calculator class.
"""

class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Adds two numbers without needing class or instance context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Multiplies two numbers and accesses a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
