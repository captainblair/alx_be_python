# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)  # convert numerator to float
        den = float(denominator)  # convert denominator to float

        result = num / den  # perform the division
        return f"The result of the division is {result}"  # return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."  # handle division by 0

    except ValueError:
        return "Error: Please enter numeric values only."  # handle non-numeric input
