#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Function Description:
	Calculate the factorial of a given number using recursive approach.

	Parameters:
	n (int): The number for which factorial is to be calculated.

	Returns:
	int: The factorial of the given number.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

