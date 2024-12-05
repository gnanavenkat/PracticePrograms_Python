#84. Write a program to print all Perfect numbers between 1 to n.
n=int(input("Enter the number to print all erfect numbers "))
i=1
while(i<=n):
    j=1
    sum=0
    while(j<i):
        if(i%j==0):
            sum=sum+j
        j=j+1
    if(i==sum):
        print(i)
    i=i+1
