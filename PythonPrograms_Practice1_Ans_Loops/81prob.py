#81. Write a program to enter any number and check whether it is Strong number or not.
n=int(input("Enter the number whether it is strong or not"))
temp=n
sum=0
while(n>0):
    d=n%10
    fact=1
    while(d>0):
        fact=fact*d
        d=d-1
    sum=sum+fact
    n=n//10
if(temp==sum):
    print("Strong number")
else:
    print("Not a strong number")
