#75. Write a program to enter any number and find the sum of first and last digit of the number.
n=int(input("Enter the number for find sum of the first and last digit"))
sum=0
last=n%10
while(n>0):
    d=n%10
    n=n//10
first=d
sum=first+last
print(sum)
