#92.Write a Python program that accepts a string and calculate the number of digits and letters.
st=input("enter the string")
digit_sum=0
letters_count=0
for i in st:
    if(i.isdigit()):
        digit_sum=digit_sum+1
    elif(i.isalpha()):
        letters_count=letters_count+1
print("Letters",letters_count)
print("Digits",digit_sum)
