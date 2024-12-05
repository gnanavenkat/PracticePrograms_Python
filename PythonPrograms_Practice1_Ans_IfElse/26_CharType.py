# Program to check if a character is an alphabet, digit, or special character

# Input a character
char = input("Enter a character: ")

# Check the type
if char.isalpha():
    print(f"{char} is an alphabet.")
elif char.isdigit():
    print(f"{char} is a digit.")
else:
    print(f"{char} is a special character.")
