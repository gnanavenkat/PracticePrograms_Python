#64. Write a program to print sum of all odd numbers between 1 to n.
n=int(input("Enter the number to print sum of all odd numbers"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        sum=sum+i
print(sum)
