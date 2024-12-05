#79. Write a program to enter any number and check whether it is Armstrong number or not.
n=int(input("Enter the number to check armstrong or not"))
sum=0
temp=n
while(n>0):
    d=n%10
    sum=sum+d**3
    n=n//10
if(sum==temp):
    print("Armstrong number")
else:
    print("Not a Armstrong number")
