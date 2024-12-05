import math

# Function to check if a number is a perfect square
def is_perfect_square(number):
    if number < 0:
        return False
    root = int(math.sqrt(number))
    return root * root == number

# Input a number
num = int(input("Enter a number: "))

# Call the function and display result
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
