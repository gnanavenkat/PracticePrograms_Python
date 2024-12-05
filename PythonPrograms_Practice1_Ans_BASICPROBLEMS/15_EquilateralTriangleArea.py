# 15_EquilateralTriangleArea.py

import math

# Input: Enter the side of the equilateral triangle
side = float(input("Enter the side of the equilateral triangle: "))

# Calculate area
area = (math.sqrt(3) / 4) * (side ** 2)

# Output: Display the area
print(f"The area of the equilateral triangle is {area:.2f}.")
