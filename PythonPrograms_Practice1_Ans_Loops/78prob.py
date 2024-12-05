#78. Write a program to enter any number and check whether it is Prime number or not.
n=int(input("Enter the number to print all Prime numbers "))
i=1
c=0
while(i<=n):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print("prime")
else:
    print("Not a prime")
