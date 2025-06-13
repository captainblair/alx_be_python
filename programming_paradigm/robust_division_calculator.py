def safe_divide(numerator, denominator):
    # Try block lets us test code that might raise an error
    try:
        # Convert both inputs to float (will raise ValueError if it's not a number)
        num = float(numerator)
        den = float(denominator)

        # Division by zero is not allowed in math, this will raise ZeroDivisionError
        result = num / den
        return f"The result of the division is {result}"  # Return the division result nicely formatted

    # If input can't be turned into a number, handle it here
    except ValueError:
        return "Error: Please enter numeric values only."  # Let the user know input was invalid

    # If denominator is zero, handle that specific error
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."  # Show division by zero error clearly
