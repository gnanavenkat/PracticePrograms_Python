# Program to check if a number is divisible by 5 and 11

# Input a number
num = int(input("Enter a number: "))

# Check divisibility
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisible by both 5 and 11.")
