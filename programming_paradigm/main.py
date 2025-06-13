import sys  # This allows us to work with command line arguments

from robust_division_calculator import safe_divide  # We bring in the function we just created

def main():
    # Check if the user gave exactly two inputs (numerator and denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")  # Show user how to use the script
        sys.exit(1)  # Exit if the input isn't valid

    numerator = sys.argv[1]       # Get the first number from the command line
    denominator = sys.argv[2]     # Get the second number from the command line

    result = safe_divide(numerator, denominator)  # Call our function to handle the division
    print(result)  # Show the result (or error message)

# Only run the main function if this file is being run directly
if __name__ == "__main__":
    main()
