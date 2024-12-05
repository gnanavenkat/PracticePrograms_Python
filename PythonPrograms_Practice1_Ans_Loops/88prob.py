#87. Write a program to find sum of all prime numbers between 1 to n.
n=int(input("Enter the number to find sum of all prime numbers"))
i=0
sum=0
while(i<=n):
    j=1
    c=0
    while(j<=i):
        if(i%j==0):
            c=c+1
        j=j+1
    if(c==2):
        sum=sum+i
        #print(i)
    i=i+1
print(sum)
