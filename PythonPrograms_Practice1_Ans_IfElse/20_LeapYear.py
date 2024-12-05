# Program to check whether a year is a leap year

# Input a year
year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
