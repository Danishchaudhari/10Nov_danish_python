"""
A simple program to calculate the area of a rectangle
following PEP 8 guidelines (indentation, comments, variables).
"""

# Define the function to calculate area
def calculate_area(length, width):
    area = length * width    # Formula for area
    return area



rectangle_length = 8.0
rectangle_width = 5.0


rectangle_area = calculate_area(rectangle_length, rectangle_width)


print(f"The area of the rectangle is: {rectangle_area}")