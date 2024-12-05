#85. Write a program to print all Strong numbers between 1 to n.
n=int(input("Enter the number to print all the strong numbers "))
i=1
while(i<=n):
    temp=i
    sum=0
    while(temp>0):
        d=temp%10
        fact=1
        while(d>0):
            fact=fact*d
            d=d-1
        sum=sum+fact
        temp=temp//10
    if(i==sum):
        print(i)
    i=i+1
