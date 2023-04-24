#list comprehension-> less line of codes for function which is working on iterable 
# syntax: newlist=[(expression(x) )(for x in old list) (if chcek)]
#oldlist=[]

# write a program to generate list of 10 numbers
result=[]
for i in range (1,11):
    result.append(i)
print(result)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# How to do it using list conprehension
result=[x for x in range(1,11)]
print(result)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# get a list of all even numbers between 1 to 50
result=[x for x in range (1,51) if x%2==0]
print(result) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# get a list of all even numbers from given list
list_a=[1,2,4,3,6,7,9]
result=[x for x in list_a if x%2==0]
print(result)#[2, 4, 6]

# convert all strigs into uppercase in given list
lista=['hi','welcome','to',"anjali's",'lab']

result=[x.upper() for x in lista]
print(result)#['HI', 'WELCOME', 'TO', "ANJALI'S", 'LAB']

# put all the negative numbers after positive numbers from given list 
list_a=[1,-1,2,-5,9,10,-6]

# result=[1,2,9,10,-1,-5,-6]
result1=[x for x in list_a if x>0]
result2=[x for x in list_a if x<0]

print(result1+result2) #[1, 2, 9, 10, -1, -5, -6]

result=[x for x in list_a if x>0]+[x for x in list_a if x<0]
print(result)#[1, 2, 9, 10, -1, -5, -6]
