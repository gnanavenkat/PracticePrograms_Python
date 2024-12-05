#71. Write a program to enter any number and check whether the number is palindrome or not.
n=int(input("Enter the number to check it is palindrome or not"))
rev=0
temp=n
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("polindrome")
else:
    print("not a polindrome")
