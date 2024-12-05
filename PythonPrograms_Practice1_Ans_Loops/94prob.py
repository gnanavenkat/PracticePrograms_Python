#94. Write a Python program to create the multiplication table (from 1 to 10) of a number
#7 x 1 = 7
#7 x 2 = 14
#7 x 3 = 21
#7 x 4 = 28
#7 x 5 = 35
#7 x 6 = 42
#7 x 7 = 49
#7 x 8 = 56
#7 x 9 = 63
#7 x 10 = 70
n=int(input("enter which table do you want to print"))
i=1
while(i<=10):
    print(n,'x',i,'=',n*i)
    i=i+1
