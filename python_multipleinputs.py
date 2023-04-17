# Python program to take multiple inputs from the user
a, b = input("Enter two of your lucky number: ").split() 
print("First lucky number is: ", a) 
print("Second lucky number is: ", b) 

#multiple inputs in Python using input
x, y = input("Enter First Name: "), input("Enter Last Name: ") 
print("First Name is: ", x) 
print("Second Name is: ", y)

#multiple inputs in Python using map
x, y = map(int, input("Enter two values: ").split())
print("First Number is: ", x) 
print("Second Number is: ", y)

#multiple inputs in Python using map
x, y = map(str, input("Enter your first and last name ").split())
print("First Name is: ", x) 
print("Second Name is: ", y)

#multiple inputs in Python using list comprehension
x, y = [x for x in input("Enter your name and age: ").split(",")]
print("Your name is: ", x) 
print("Your age is: ", y)
