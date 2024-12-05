#67. Write a program to enter any number and calculate product of its digits.
n=int(input("Enter the number for find product of the digits"))
pro=1
while(n>0):
    d=n%10
    pro=pro*d
    n=n//10
print("The product of the digits is : ",pro)
