# dictionary in python
dict1 = {} #b Blank disctionary
print(type(dict1)) #<class 'dict'>

# How to insert a value in dict
dict2 = {}
dict2['name']=['Anjali']
dict2['age']=26
dict2['skills']=['python','sql','hadoop']
dict2['states visited']=('karnataka','kerala','tamilnadu')
dict2[45]='random key'
print(dict2) #{'name': ['Anjali']} #{'name': ['Anjali'], 'age': 26, 'skills': ['python,sql,hadoop'], 'states visited': ('karnataka', 'kerala', 'tamilnadu'), 45: 'random key'}
dict3={'color':'purple','nationality':'India'}
dict2['other_details']=dict3
print(dict2)

# How to check the length of the dictionary
print(len(dict2))

# How to access value of a particular key
print(dict2['name'])
# print(dict2['skills'])


# How to print the 2ndary skillset of Anjali
temp = dict2['skills']
print(temp [1]) #why to add this extra step here in dict--> safely assume that this expression gives list as output

# How to print the 2ndary skillset of Anjali in single step
print(dict2['skills'][1])

# how to access the nationality of Anjali
print(dict3['nationality']) #India
print(dict2['other_details']['nationality']) #India

# how to update the value on a  particular key
dict2['age']=30
print(dict2)

# how to know the keys of the dict
total_keys=dict2.keys()
print("total keys in dict2:",total_keys) #total keys in dict2: dict_keys(['name', 'age', 'skills', 'states visited', 45, 'other_details'])

total_keys=list(dict2.keys())
print("total keys in dict2:",total_keys)

# how to know the values of the dict
total_values=list(dict2.values())
print("total keys in dict2:",total_values)

# How to iterate on dictionary?
for k,v in  dict2.items():
    print("keys is =",k,'and value is =',v,)

#compare dictionary??

dict3={'a':1,'b':2,'c':3}
dict4={'b':2,'c':3,'a':1,}
print(dict3==dict4) # True

dict5={'a':1,'b':2,'c':3}
dict6={'b':10,'c':3,'a':1,}
print(dict5==dict6) # False

# How to delete the key value pair from the dictionary?
print(dict2)
del dict2['age']
del dict2[45]
print(dict2)

#How to check if key exist in dictionary or not ?
print(dict2.get('skills'))
# print(dict2.has_key('skills')) # does not work in python 3 

keys_in_dict = list(dict2.keys())
if 'skills' in keys_in_dict:
    print(True)
else:
    print(False) #True
