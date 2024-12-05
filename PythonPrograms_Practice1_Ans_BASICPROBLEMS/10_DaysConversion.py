# 10_DaysConversion.py

# Input: Enter the number of days
days = int(input("Enter the number of days: "))

# Convert to years, weeks, and remaining days
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

# Output: Display the result
print(f"{days} days = {years} years, {weeks} weeks, and {remaining_days} days.")
