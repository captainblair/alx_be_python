# main.py

import sys  # import sys module to read command line arguments
from robust_division_calculator import safe_divide  # import your function

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")  # help message
        sys.exit(1)

    numerator = sys.argv[1]  # get first number
    denominator = sys.argv[2]  # get second number

    result = safe_divide(numerator, denominator)  # call function
    print(result)  # show result

if __name__ == "__main__":
    main()  # run main
