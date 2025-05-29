# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern:"))

# Initialize the row counter
row = 0

# Outer loop (while) to iterate through rows
while row < size:
    # Inner loop (for) to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after one row is complete
    row += 1