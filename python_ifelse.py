# How to use If-Else in python
# control transfer conditions
x = 10
y = 5
if x==y:
    print("yes the value of x is equal to value of y")
else:
    print("No the value of x is not equal to value of y")
# Is it mandatory to use else block with if ?
#control + / buttons on window will help in commenting or uncommenting entire block of code 
# a = 50
# if a==50:
#     print("a is equals to 50!!")

# print("Bye !!!")

a = 40
if a==50:
    print("a is equals to 50!!")

print("Bye !!!")

#Nested if-else 

marks = 88
if marks>=90:
    print("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A")
elif marks>=70 and marks<80:
    print("Grade B+")
elif marks>=60 and marks<70:
    print("Grade B")
else:
    print("Grade C")

#assignment 1 q 22
age = int(input("Enter your age:"))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")

#assignment 1 q 24
# Python program to find the largest number among the three input numbers
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

if (n1 >= n2) and (n1 >= n3):
   largest = n1
elif (n2 >= n1) and (n2 >= n3):
   largest = n2
else:
   largest = n3

print("The largest number is", largest)
