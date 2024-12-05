# Program to calculate electricity bill

# Input customer number and units consumed
customer_number = int(input("Enter the customer number: "))
units = float(input("Enter the number of units consumed: "))

# Calculate charges
if units <= 50:
    charges = units * 1.35
elif units <= 100:
    charges = 50 * 1.35 + (units - 50) * 2.60
elif units <= 200:
    charges = 50 * 1.35 + 50 * 2.60 + (units - 100) * 2.85
elif units <= 300:
    charges = 50 * 1.35 + 50 * 2.60 + 100 * 2.85 + (units - 200) * 4.50
elif units <= 400:
    charges = 50 * 1.35 + 50 * 2.60 + 100 * 2.85 + 100 * 4.50 + (units - 300) * 5.00
else:
    charges = 50 * 1.35 + 50 * 2.60 + 100 * 2.85 + 100 * 4.50 + 100 * 5.00 + (units - 400) * 5.75

# Add minimum charges
charges = max(charges, 20.0)

# Display the result
print(f"Customer Number: {customer_number}")
print(f"Total Amount to be Paid: Rs.{charges:.2f}")
