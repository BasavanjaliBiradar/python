# Lambda functions are like inline functions
# inline function =anonymous functions bez no specific name ,,no user defined functions
# shorter logic temp logics ,,we dont need def keyword and logical expression only 
# syntax: lambda argument:evaluating expression
# How to create lambda function
# first normal function to add integer 5 in given number
def add_5(num):
    result=num+5
    return result
x=7
print(add_5(x)) #12

# second using lambda function to add integer 5 in given number
lambda_add_five =lambda y :y + 5 #y + 5 this automatically return to the lambda argument
x=10
print(lambda_add_five(x))# 15

# lambda functuon rto add 2 numbers/ more than one argument/parameters
lambda_add=lambda num1,num2:num1+num2
num1=12
num2=10
print(lambda_add(num1,num2))# 22

# write a lambda function to concatinate two strings
lambda_add_string=lambda str1,str2:str1+str2
str1="Anjali"
str2="Vivek"
print(lambda_add_string(str1,str2))

# write a lambda function to calculate maximum of two numbers
lambda_max=lambda num3,num4:num3 if num3>num4 else num4
num3=10
num4=11
print(lambda_max(num3,num4))

# write a normal function to calculate maximum of two numbers
def max_of_num(x,y):
    if(x>y):
        return x
    else:
        return y
a=5
b=4
print(max_of_num(a,b))

# How to work with map(),filter(),reduce()

# map() ->x1,x2,x3,x4+ mapping function to set-> in output y1,y2,y3,y4
# trying to modify the values of individual value in the set using simple expression using lambda function again

#impletement map function
list1=[1,2,3,4,5,6,7,8,9]

# result =[1,4,9,16,25,36,49,64,81]

square_num=lambda x:x*x

square_list=list(map(square_num,list1)) # type casting output to list format
print(square_list)

# interior working of map function used above
# for i in list1:
#     print(square_num(i))

# Add sequenctial respective elements in two given lists
lista=[1,2,3,4,5]
listb=[5,4,3,2,1]
sum_off=lambda x,y:x+y
add_off=list(map(sum_off,lista,listb))
print(add_off)

#REDUCE function->at the end we will get one final value(not a iterable),
# it just reduces the values given in a iterable to a single value using some expression

# how to use reduce function?? it is used in func tools
# add all the elements in list 
import functools
list_x=[1,2,3,4,5]
# result=0
# result=result+i
add_two_nums=lambda x,y:x+y
result=functools.reduce(add_two_nums,list_x)
print(result) # 15

# multiplication of all elements in list
list_x=[1,2,3,4,5]
# result=0
# result=result+i
add_two_nums=lambda x,y:x*y
result=functools.reduce(add_two_nums,list_x)
print(result) # 120

# filter function -> uses lambda function to check weather particular eliment is a part of o/p or not 
# how to use filter()?
seq=[1,2,5,6,7,10]
filter_odd=lambda x:x%2!=0
result=list(filter(filter_odd,seq))
print(result) #[1, 5, 7]

# create list of only even elements

seq=[1,2,5,6,7,10]
filter_even=lambda x:x%2==0
result=list(filter(filter_even,seq))
print(result) #[2, 6, 10]

# in map=number of i/p and o/p are same
# in reduce =number of i/p is more number of o/p is one
# in filter number of i/p o/p are n and m



