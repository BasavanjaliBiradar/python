#declare empty list
L1 =[]
print(type(L1))

# Insert values in list 
L1.append(5)
L1.append(10)
L1.append(30)
L1.append(15)
print(L1)

# Create a list of 10000 numbers start from 1 to 10000
int_list =[]
for num in range(1,10000):
    int_list.append(num)
print(int_list)

# How to calculate the length of the list?
len_of_list =len(int_list)
print(len_of_list)

# How to check are equal to each other
list1=[1,"Anju",26,"female"]

list2=[1,"Anju",26,"female"]
print("lists are equal??", list1==list2)

#list concat
list4 = [1,2,3,4,5]
list5 = [80,90,100,110]
result = list4+list5
print(result)

#How to access list values
list6 = [10,15,20,25,30,35]

# Print all the elements of given list
for num in list6:
    print(num)

# Print 3rd element of list6
print(list6[2]) 
# syntax = list_name[index]
print(list6[0]) 
print(list6[1]) 
print(list6[2]) 
print(list6[3]) 
print(list6[4]) 
print(list6[5]) 

# What will happen?
print(list6[100]) # Index error: list index out of range

list7 = [1,"Vivek",1000]
print(list7)

# How to update the value of list index item?
# updtae Vivek to Basavanjali
list7[1]= "Basavanjali"
print(list7)

# How to print list elements using length?
for index in range(0,len(list7)): # range (0,3)->[0,1,2]
    print(list7[index])



list8 = [1,2,50,"ineuron",[6,6,6],"vicky"]
print(len(list8))

#difference between append() and extend()

list9 = [20,30,40]
list10 = ["hello","hi","bye","bye"]
result1 = list9.append(list10)
print("output of append:", list9) #output of append: [20, 30, 40, ['hello', 'hi', 'bye', 'bye']]
print("length after append:",len(list9))# output:4


list11 = [20,30,40]
list12 = ["hello","hi","bye","bye"]
result2 = list11.extend(list12)
print("output of extend:", list11) # output of extend: [20, 30, 40, 'hello', 'hi', 'bye', 'bye']
print("length after append:",len(list11)) # output:7

# List slicing
list13 = [20,30,40,50,60,80,90]
# syntax-> listname[startindex:endindex:step(optional)]
print(list13[0:]) # [20, 30, 40, 50, 60, 80, 90]
print(list13[3:]) # [50, 60, 80, 90]
print(list13[:]) # [20, 30, 40, 50, 60, 80, 90]
print(list13[0:3]) # [20, 30, 40] # end intex is always exclusive
print(list13[0:4]) # [20, 30, 40, 50]
print(list13[2:6]) # [40, 50, 60, 80]
print(list13[:4]) # [20, 30, 40, 50]
print(list13[0::2]) # [20, 40, 60, 90]
print(list13[0:5:2]) # [20, 40, 60]

# Traverse list in backword direction
# how to print the last value of the list? without knowing the length of the list 
# 2 ways to print the last value 
# 1
print(list13[len(list13)-1]) # output = 90
print(list13[-1]) # negative index -1 means the last element of the list # outpiut 90

# print 2nd last element in the list 
print(list13[-2]) # negative index -2 means the last 2nd element of the list # outpiut 80

# print input list in reverse direction
print(list13[-1:]) #output [90]--> 2nd element in traversing code is given blank and by defalt the step parameter is positive
print(list13[-1::-1]) # output [90, 80, 60, 50, 40, 30, 20]--> step should be given -1


#lists are mutable can change during runtime
