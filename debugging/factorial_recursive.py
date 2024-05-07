#!/usr/bin/python3
import sys

# Function description: Computes the factorial of a given number recursively.
# Parameters:
#   - n: An integer representing the number for which factorial is to be computed.
# Returns:
#   - The factorial of the input number.

def factorial(n):
    # Base case: factorial of 0 is 1.
    if n == 0:
        return 1
    # Recursive case: compute factorial by multiplying n with factorial(n-1).
    else:
        return n * factorial(n-1)

# Get the factorial of the number provided as a command-line argument.
f = factorial(int(sys.argv[1]))
print(f)
