# Program to calculate gross salary

# Input basic salary
basic_salary = float(input("Enter basic salary: "))

# Determine HRA and DA
if basic_salary <= 10000:
    hra = basic_salary * 0.20
    da = basic_salary * 0.80
elif basic_salary <= 20000:
    hra = basic_salary * 0.25
    da = basic_salary * 0.90
else:
    hra = basic_salary * 0.30
    da = basic_salary * 0.95

# Calculate gross salary
gross_salary = basic_salary + hra + da

# Display result
print(f"Gross Salary: {gross_salary}")
