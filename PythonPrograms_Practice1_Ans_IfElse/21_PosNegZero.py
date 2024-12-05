# Program to check whether a number is positive, negative, or zero

# Input a number
num = float(input("Enter a number: "))

# Check and display result
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"The number is zero.")
