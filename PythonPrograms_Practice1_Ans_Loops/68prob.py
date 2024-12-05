#68. Write a program to enter any number and calculate sum of all natural numbers between 1 to n.
n=int(input("Enter the number to find the sum of all natural number "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("the sum of the natural numbers from 1 to ",n,"is: ",sum)
