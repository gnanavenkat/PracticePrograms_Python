#76. Write a program to enter any number and print all factors of the number.
n=int(input("Enter the number for to print the factors"))
for i in range(1,n+1):
    if (n%i==0):
        print(i)
