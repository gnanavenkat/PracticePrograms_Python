# Program to check if a triangle is valid based on its sides

# Input sides
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Check validity
if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
