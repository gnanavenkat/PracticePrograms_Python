# Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Input a number
num = float(input("Enter a number: "))

# Call the function and display result
print(f"The number is {check_number(num)}.")
