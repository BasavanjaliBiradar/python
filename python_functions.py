#functions are used bez reusablility of the particular code
# functions in python
# what about len()

# examples of inbuilt function
# list1=[1,2,3,4,5,6]
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
    return "message from bot !!!"
bot_message() # no output bez no print in function
print(bot_message())
result=bot_message()
print("output from bot message:",result)
