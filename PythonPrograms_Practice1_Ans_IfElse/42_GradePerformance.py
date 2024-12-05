# Program to display performance level based on grade character

# Input grade character
grade = input("Enter a grade (O, A, B, C, F): ").upper()

# Map grade to performance
performance = {
    "O": "Outstanding",
    "A": "Very Good",
    "B": "Good",
    "C": "Average",
    "F": "Fail"
}

# Display performance
print(performance.get(grade, "Invalid grade."))
