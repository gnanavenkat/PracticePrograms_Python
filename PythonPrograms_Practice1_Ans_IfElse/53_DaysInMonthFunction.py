# Function to determine number of days in a month
def days_in_month(month):
    days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return days.get(month, "Invalid month number.")

# Input month number
month = int(input("Enter the month number (1-12): "))

# Call the function and display result
print(f"Days: {days_in_month(month)}")
