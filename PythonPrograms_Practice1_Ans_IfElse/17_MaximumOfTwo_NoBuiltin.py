# Program to find the maximum between two numbers without using built-in functions

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Find the maximum without using built-in functions
if num1 > num2:
    maximum = num1
else:
    maximum = num2

# Display the result
print(f"The maximum of {num1} and {num2} is {maximum}")
