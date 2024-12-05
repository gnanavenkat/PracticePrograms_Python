# Program to count total number of notes in a given amount

# Input the amount
amount = int(input("Enter the amount: "))

# Define note denominations
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Count the notes
note_count = {}
for note in notes:
    note_count[note] = amount // note
    amount %= note

# Display the count of notes
for note, count in note_count.items():
    if count > 0:
        print(f"{note}: {count}")
