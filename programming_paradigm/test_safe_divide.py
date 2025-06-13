import unittest
from robust_division_calculator import safe_divide

class TestSafeDivide(unittest.TestCase):
    def test_valid_division(self):
        self.assertEqual(safe_divide("10", "2"), "The result of the division is 5.0")

    def test_zero_division(self):
        self.assertEqual(safe_divide("10", "0"), "Error: Cannot divide by zero.")

    def test_non_numeric_input(self):
        self.assertEqual(safe_divide("hello", "5"), "Error: Please enter numeric values only.")

if __name__ == '__main__':
    unittest.main()
