# Program to display month name using a dictionary

# Input month number
month = int(input("Enter the month number (1-12): "))

# Month dictionary
month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"
}

# Display result
print(month_dict.get(month, "Invalid month number."))
