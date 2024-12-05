# Program to calculate pay with overtime

# Input hours and rate
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Calculate pay
if hours > 40:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    pay = hours * rate

# Display the result
print(f"Pay: {pay}")
