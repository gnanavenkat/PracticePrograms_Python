# Program to check if a character is uppercase or lowercase

# Input a character
char = input("Enter a character: ")

# Check case
if char.isupper():
    print(f"{char} is an uppercase alphabet.")
elif char.islower():
    print(f"{char} is a lowercase alphabet.")
else:
    print(f"{char} is not an alphabet.")
