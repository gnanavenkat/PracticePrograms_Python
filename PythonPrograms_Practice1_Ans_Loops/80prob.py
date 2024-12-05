#80. Write a program to enter any number and check whether it is Perfect number or not.
n=int(input("Enter the number to print all erfect numbers "))
i=1
sum=0
while(i<n):
    if(n%i==0):
        sum=sum+i
        
    i=i+1
if(sum==n):
    print("perfect")
else:
    print("Not a perfect")
