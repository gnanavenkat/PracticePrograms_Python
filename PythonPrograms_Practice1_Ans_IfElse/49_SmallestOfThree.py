# Program to find the smallest of three numbers

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the smallest
smallest = min(num1, num2, num3)

# Display result
print(f"The smallest of {num1}, {num2}, and {num3} is {smallest}.")
