#70. Write a program to enter any number and print its reverse.
n=int(input("Enter the number and print its reverse"))
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
print("the reverse of the given number is: ",rev)
