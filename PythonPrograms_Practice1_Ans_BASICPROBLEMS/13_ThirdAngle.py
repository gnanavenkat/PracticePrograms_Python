# 13_ThirdAngle.py

# Input: Enter two angles of a triangle
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))

# Calculate the third angle
third_angle = 180 - (angle1 + angle2)

# Output: Display the third angle
print(f"The third angle of the triangle is {third_angle}.")
