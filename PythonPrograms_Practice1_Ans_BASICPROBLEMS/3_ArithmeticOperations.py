# 3_ArithmeticOperations.py

# Input: Enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2 if num2 != 0 else 'Undefined (division by zero)'}")
print(f"Modulus: {num1 % num2 if num2 != 0 else 'Undefined (division by zero)'}")

