# #palindrome string=Madam==reverse(madam) its is a palindrome string
a=input("enter the string to check weather the string is palindrome or not:")#madam
b=a[-1::-1]
if(a==b):
    print(f"{a} is a palindrome string")
else:
    print(f"{a} is not a palindrome string")#madam is a palindrome string
