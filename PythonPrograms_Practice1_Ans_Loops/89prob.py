#88. Write a program to print Fibonacci series up to n terms.
n=int(input("Enter the number to print Fibonacci series"))
k=2
i=0
j=1
print(i)
while(k<=n):
    f=i+j
    i=j
    j=f
    print(i)
    k=k+1
