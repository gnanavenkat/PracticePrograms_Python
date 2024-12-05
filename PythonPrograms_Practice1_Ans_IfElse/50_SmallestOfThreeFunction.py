# Function to find the smallest of three numbers
def smallest_of_three(a, b, c):
    return min(a, b, c)

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function and display result
print(f"The smallest number is {smallest_of_three(num1, num2, num3)}.")
