#) Write a Python program to create a module named math_module.py that contains functions to calculate the square root and factorial of a number. Then, import the module and use the functions to perform calculations.

import math

def calculate_square_root(number):
    return math.sqrt(number)

def calculate_factorial(number):
    return math.factorial(number)

# Example usage
num = 16
print(f"The square root of {num} is: {calculate_square_root(num)}")
num = 5
print(f"The factorial of {num} is: {calculate_factorial(num)}")