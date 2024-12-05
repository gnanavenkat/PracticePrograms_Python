# Program to check if an alphabet is a vowel or consonant

# Input an alphabet
char = input("Enter an alphabet: ").lower()

# Check vowel or consonant
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print(f"{char} is not an alphabet.")
