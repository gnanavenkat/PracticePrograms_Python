# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b if b != 0 else "Undefined (division by zero)"

# Menu-driven program
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1/2/3/4): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1:
    print(f"Result: {add(num1, num2)}")
elif choice == 2:
    print(f"Result: {subtract(num1, num2)}")
elif choice == 3:
    print(f"Result: {multiply(num1, num2)}")
elif choice == 4:
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid choice.")
