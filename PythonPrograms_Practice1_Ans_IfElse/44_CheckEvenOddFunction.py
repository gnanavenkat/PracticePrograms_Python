# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input a number
num = int(input("Enter a number: "))

# Call the function and display result
print(f"{num} is {check_even_odd(num)}.")
