#82. Write a program to print all Prime numbers between 1 to n.
n=int(input("Enter the number to print all Prime numbers "))
i=1
while(i<=n):
    j=1
    c=0
    while(j<=i):
        if(i%j==0):
            c=c+1
        j=j+1
    if(c==2):
        print(i)
    i=i+1
