#69. Write a program to enter any number and find its first and last digit.
n=int(input("Enter the number for find sum of the first and last digit"))
last=n%10
while(n>0):
    d=n%10
    n=n//10
first=d
print("the first number in the given number is: ",first)
print("the last number in the given number is: ",last)
