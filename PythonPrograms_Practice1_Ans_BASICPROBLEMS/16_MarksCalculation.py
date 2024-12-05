# 16_MarksCalculation.py

# Input: Enter marks for five subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate total, average, and percentage
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

# Output: Display the results
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage:.2f}%")
