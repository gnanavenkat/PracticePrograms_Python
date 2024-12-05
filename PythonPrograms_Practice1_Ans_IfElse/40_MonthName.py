# Program to display month name based on number

# Input month number
month = int(input("Enter the month number (1-12): "))

# Map of months
months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# Display result
if 1 <= month <= 12:
    print(f"The month is {months[month - 1]}")
else:
    print("Invalid month number.")
