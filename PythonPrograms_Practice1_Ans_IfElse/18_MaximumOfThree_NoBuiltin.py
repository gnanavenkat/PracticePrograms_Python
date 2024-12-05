# Program to find the maximum between three numbers without using built-in functions

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum without using built-in functions
if num1 > num2:
    if num1 > num3:
        maximum = num1
    else:
        maximum = num3
else:
    if num2 > num3:
        maximum = num2
    else:
        maximum = num3

# Display the result
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")
