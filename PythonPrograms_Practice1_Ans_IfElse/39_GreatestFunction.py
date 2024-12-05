# Function to find the greatest of three numbers
def greatest(a, b, c):
    return max(a, b, c)

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call function and display result
print(f"The greatest number is {greatest(num1, num2, num3)}")
