# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print asterisks in the row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1

