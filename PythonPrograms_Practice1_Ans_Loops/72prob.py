#72. Write a program to enter any number and print it in words.
n=int(input("Enter the number and print it in words"))
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
while(rev>0):
    d=rev%10
    if(d==0):
        print("Zero",end=' ')
    elif(d==1):
        print("one",end=' ')
    elif(d==2):
        print("Two",end=' ')
    elif(d==3):
        print("Three",end=' ')
    elif(d==4):
        print("Four",end=' ')
    elif(d==5):
        print("Five",end=' ')
    elif(d==6):
        print("Six",end=' ')
    elif(d==7):
        print("Seven",end=' ')
    elif(d==8):
        print("Eight",end=' ')
    elif(d==9):
        print("Nine",end=' ') 
    rev=rev//10
