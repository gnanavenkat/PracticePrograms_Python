# 6_CircleMeasurements.py

import math

# Input: Enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Output: Display the results
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")

