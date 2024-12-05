# Program to check if a triangle is valid based on its angles

# Input angles
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Check validity
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
