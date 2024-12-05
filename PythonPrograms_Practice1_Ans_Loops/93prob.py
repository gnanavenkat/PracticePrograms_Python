#93. Write a Python program to construct the following pattern, using a nested loop number
n=int(input("Enter the number of rows do you want to print the pattern"))
row=1
while(row<=n):
    col=1
    while(col<=row):
        print(row,end=' ')
        col=col+1
    print(end='\n')
    row=row+1
