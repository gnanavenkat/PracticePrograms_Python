#83. Write a program to print all Armstrong numbers between 1 to n.
n=int(input("Enter the number to print all the Armstrong numbers "))
i=1
while(i<=n):
    sum=0
    temp=i
    while(temp>0):
        d=temp%10
        sum=sum+d**3
        temp=temp//10
    if(sum==i):
        print(i)
    i=i+1
    
