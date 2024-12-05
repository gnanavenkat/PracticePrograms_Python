# Program to calculate percentage and grade based on marks

# Input marks for five subjects
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
biology = float(input("Enter marks in Biology: "))
maths = float(input("Enter marks in Mathematics: "))
computer = float(input("Enter marks in Computer: "))

# Calculate total, percentage, and grade
total = physics + chemistry + biology + maths + computer
percentage = (total / 500) * 100

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

# Display results
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
