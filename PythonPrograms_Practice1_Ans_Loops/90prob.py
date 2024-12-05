#90. Write a python program to compute sum of the factorials of each digit of a given integer. Write a separate function for calculating the factorial of a number.
num=int(input("Enter the numberto compute sum of the factorials of each digit of a given number"))
sum=0
while(num>0):
    d=num%10
    fact=1
    while(d>0):
        fact=fact*d
        d=d-1
    sum=sum+fact
    num=num//10
print(sum)
