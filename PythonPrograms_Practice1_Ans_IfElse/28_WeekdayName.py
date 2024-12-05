# Program to print the weekday name for a given week number

# Input week number
week_num = int(input("Enter a week number (1-7): "))

# Map week number to name
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Display the result
if 1 <= week_num <= 7:
    print(f"The day is {weekdays[week_num - 1]}.")
else:
    print("Invalid week number.")
