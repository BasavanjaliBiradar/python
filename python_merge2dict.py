# Python program to merge two dictionary
# using | operator
d1 = {'Anjali': 2000, 'Vivek': 500000}
d2 = {'Aruna': 4000, 'Arvind': 3000}

# print(d1 | d2)
# using **operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1,**dict_2})#{1: 'a', 2: 'c', 4: 'd'}
# Using copy() and update()
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)#{2: 'b', 4: 'd', 1: 'a'}
