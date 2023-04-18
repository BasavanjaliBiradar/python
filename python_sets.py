# Sets in python

set1=set()
print(type(set1)) #<class 'set'>

# Representing and creating a set 
set3={1,2,3,4,5,2,1,4}
print(set3) #{1, 2, 3, 4, 5}
print(type(set3)) #<class 'set'>

#dictionary
set4={}
print(type(set4)) #<class 'dict'>

# Remove the dublicates from the list 
list1=[1,2,3,4,1,2,3,4,5,6,7,8,1]
set2=set(list1)
print(set2) #{1, 2, 3, 4, 5, 6, 7, 8}
# print(set2[0]) #TYPE ERROR

# How to iterate elements in the set
for num in set2:
    print(num)

#convert output of set into list
list1=[1,2,3,4,5,6,7,8,1,2,3,4,5,1,2,3,4,5]
set5=list(set(list1))
print(set5)
print(set5[-1]) #8

# How to add /insert elements in the set 
set6 =set()
set6.add(1)
set6.add(1)
set6.add(2)
set6.add(5)
set6.add(2)
set6.add(1)
set6.add(2)
print(set6) #{1, 2, 5}

# How to update the elements in the set-->use of update method
temp=[1,2,3,4,5,1,2,3,4,5,1,2,3]
set6.update(temp)
print(set6) #{1, 2, 3, 4, 5}

# How to check length of the set
print(len(set6)) #5

#set operations
set_a={1,2,3,4,5,6}
set_b={3,6,8,9,10}

# union operation
print(set_a | set_b) #{1, 2, 3, 4, 5, 6, 8, 9, 10}

# intersection operation
print(set_a & set_b) #{3, 6}

# A-B? 
# Differnce in sets
print(set_a - set_b) #{1, 2, 4, 5} print all elements in set_a except the elements present in set_b
print(set_b - set_a) #{8, 9, 10} print all elements in set_b except the elements present in set_a

# Comparision in sets
setx={1,2,3,4,5}
sety={1,2,3,5,4,5,1}
print(setx ==sety) #True
setz={1,2,3,5,4,5,6}
print(setx ==setz) #False

set_m={5,6,7,1,2,4}
print(set_m) #{1, 2, 4, 5, 6, 7}
