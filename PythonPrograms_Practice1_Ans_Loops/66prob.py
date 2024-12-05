#66. Write a program to enter any number and calculate sum of its digits.
n=int(input("Enter the number for find sum of the digits"))
sum=0
while(n>0):
    d=n%10
    sum=sum+d
    n=n//10
print("The sum of the digits is : ",sum)
