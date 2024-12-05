#77. Write a program to enter any number and calculate its factorial.
n=int(input("Enter the number for to print the factorial"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print(fact)
