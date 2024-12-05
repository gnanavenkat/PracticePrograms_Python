# Program to print the number of days in a month

# Input month number
month = int(input("Enter the month number (1-12): "))

# Days in each month
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Determine days
if 1 <= month <= 12:
    print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number.")
