# Declare and assign variables in python
int_var = 10
float_var = 18.25

# int a =10:// this is code in c, java or other programing language,but in python no need to mention explicitly the data type
string_var = 'Anjali Biradar' # or another way "Anjali Biradar"
bool_var = True #if we want to assign false then it should be like False

# Function in python for output 
#Function does what? they might or might not accept some parameters
print("Hello Queen Anjali!!!")

#print variable values in python
print("value of integer:" ,int_var," -- Result Done!!!")
print("value of float:", float_var, " -- Result Done!!!")
print("value of string:", string_var, " -- Result Done!!!")
print("value of bool:", bool_var, " -- Result Done!!!")

# How to check the datatype of any variable in python
# we can use type() function
print("type of int_var?",type(int_var), "-- Result Done!!!")
print("type of float_var?", type(float_var), "-- Result Done !!!")
print("type of string_var?", type(string_var), "-- Result Done!!!")
print("type of bool_var?", type(bool_var), "-- Result Done!!!")

# How to do the type casting in python
#int(), float(),bool(),str()
int_var = int_var + 10 # int_var = 10 + 10 =20
print("Updated value of int_var:",int_var)

casted_int_var = float(int_var)
print("int to float typecasting for int_var:",casted_int_var)
casted_float_var = int(float_var)
print("float to int typecasting for float_var:",casted_float_var)
numeric_str = "123"
#numeric_str = numeric_str + 50 it is invalid bez 123 is the str and 50 is the int type ->str to str can be added not str and int
#numeric_str = numeric_str + "50"
#print("value of numeric_str is:",numeric_str)
numeric_str = int(numeric_str) + 50 #  numeric_str = int("123") + 50 =173
print("value of numeric_str is:",numeric_str)

# How to take the  inputs on python?
# we can use input() function i.e user input 
name = input()
age = input()
print("username =",name)
print("userage =",age)
to give the inputs here select run python file not run code while running 
python file_name.py this is command used in the background when you select run python file while running

#another way to take user input with custom message
    name = input("Enter value for name =")
    age = input("Enter value for age =")
    print("username =",name)
    print("userage =",age)
    print("type of name:", type(name))# <class str>
    print("type of age:", type(age))# <class str>

    
#convert type of data during the input
name = input("Enter value for name =")
age = int(input("Enter value for age ="))# function into function
print("username =",name)
print("userage =",age)
print("type of name:", type(name))#<class str>
print("type of age:", type(age))#<class int>
