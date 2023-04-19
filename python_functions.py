#functions are used bez reusablility of the particular code
# functions in python
# what about len()

# examples of inbuilt function
list1=[1,2,3,4,5,6]
print("maximum number from list:",max(list1)) # maximum number from list: 6
print("minimum number from list:",min(list1)) # minimum number from list: 1
print("sum number from list:",sum(list1)) # sum number from list: 21

# How do functions work?
# they may or maynot accepts the input parameters
# they may or maynot return any output

# example of a function which doesn't accept any parameter and doesn't return anything
def welcome_message(): #def is a keyword to define your functions
    print("welcome to basvanjali's lab!!!") # no output without function call

welcome_message() # function calling # output=welcome to basvanjali's lab!!!

# example of a function which doesn't accept any parameter and does return somethingthing
def bot_message():
    print("message from boy using print!!!")
    return "message from bot !!!"
bot_message() # no output bez no print in function
print(bot_message())
result=bot_message()
print("output from bot message:",result)

# example of a function which accept some parameter and does return some values
def avg_of_two_numbers(a,b):
    avg_result=(a+b)//2
    return avg_result

num1=10
num2=15
output=avg_of_two_numbers(num1,num2)
print(output) #12

# example of a function which accept some parameter and does return some values
def avg_of_two_numbers(a,b):
    count=2
    print("first value:",a) #first value: 10
    print("last value:",b) #last value: 15
    avg_result=(a+b)/2
    return avg_result

num1=10
num2=15
output=avg_of_two_numbers(num1,num2)
print(output) #12

#output=avg_of_two_numbers(num1) # error missing 1 required possitional argument b

# write a function to calculate the factorial of a num?
def factorial(n):
    if n ==0 or n==1:
        return 1
    result=1
    for num in range (1,n+1):
        result =result*num
    return result
x=5
ans=factorial(x)
print("factorial of number",x,"=",ans) #factorial of number 5 = 120

x=0
ans=factorial(x)
print("factorial of number",x,"=",ans) #factorial of number 0 = 1

# How to return multiple values from function
# a=2
# b=3
# c=5
a,b,c=2,3,5
print("value of a is:",a) #value of a is: 2
print("value of b is:",b) #value of b is: 3
print("value of c is:",c) #value of c is: 5

def square_and_cube(n):
    sqr=n*n
    cube=n*n*n
    return sqr,cube

num=3
sqr_ans,cube_ans=square_and_cube(num)
print("square of ",num,"=",sqr_ans) #square of  3 = 9
print("cube of ",num,"=",cube_ans) #cube of  3 = 27

# how to create optional arguments in python functions

def multiply(a,b=3):
    result= a*b
    return result
num1=5
num2=10
print(multiply(num1,num2))#50

# if num2 is not given 
print(multiply(num1))#15
print(multiply(num2))#30


# def multiply(a=3,b):#SyntaxError: non-default argument follows default argument

def multiply(a,b=5,c=10):# no error
    result=a*b*c
    return result
#what if we have more than 2 
num1=5
num2=10
num3=2
print(multiply(num1,num2,num3))#100
print(multiply(num1,num2))#500
print(multiply(num2,num3))#200
print(multiply(num3))#100

#Non-key value arguments
# pass numbers as a dynamic list from here'
def example_nonkeyed_args(*argv):# *argv act as a list for you
    for param in argv:
        print(param)

example_nonkeyed_args('hello',10, 'welcome','to',"anjali's lab")

print(type(example_nonkeyed_args))#<class 'function'>

# when python need to connect to any database then we need host name,password,port,

# connect_to_db('172.80.80.80','SUMA@990',9021)# USER MAY INPUT IN ANOTHER ORDER LEADS TO FAILING OFCODE

# key value arguments in python
def example_of_kwargs(**kwargs):
    print("value of host:",kwargs ['hostid'])
    print("value of portnumber:",kwargs ['portnumber'])
    print("value of password:",kwargs ['password'])
for k,v in kwargs.items():
        print("key is:",k,"vlaue is:",v)

example_of_kwargs( hostid='170.80.8080',password='suma@880',portnumber=9870 )
