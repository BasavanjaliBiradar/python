#  tuple is immutable cannot do changes during the run time only differnce between list and tuple
# dont want to update some attributes or values which are critical -> use of tuple --> fix and freez the values
t1 = () # empty tuple
# print(t1.append(5)) # error -->'tuple' object has no attribute 'append'
# t1[0] = 21 # error -->'tuple' object does not support item assignment

t2 = (20,30,40,50)
print(len(t2)) # output = 4

# Indexing also works for tuple
# access 3rd element from tuple
print(t2[2]) # output = 40

# Indexing works
# slicing works
# Iteration also works
# length function also works
