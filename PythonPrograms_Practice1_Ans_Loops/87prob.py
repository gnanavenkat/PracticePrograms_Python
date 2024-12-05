#86. Write a program to enter any number and print its prime factors.
n=int(input("Enter any number and print its prime factors"))
i=1
while(i<=n):
    if(n%i==0):
        j=1
        c=0
        while(j<=i):
            if(i%j==0):
                c=c+1
            j=j+1
        if(c==2):
            print(i)
    i=i+1
