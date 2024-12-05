# Program to check if a number is divisible by 4 and 9

# Input a number
num = int(input("Enter a number: "))

# Check divisibility
if num % 4 == 0 and num % 9 == 0:
    print(f"{num} is divisible by both 4 and 9.")
else:
    print(f"{num} is not divisible by both 4 and 9.")
