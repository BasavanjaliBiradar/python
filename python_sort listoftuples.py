# Python program to sort a list of tuples by second item.
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

X = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
print("my original tuple:",X)
X.sort()
print("sorted list of tuple on the first element:",X)
X.sort(reverse=True)# first element in reverse order
print("sorted list of tuple on the first elementin reverse order:",X)
# # BASED ON 2ND ELEMENT
X.sort(key=lambda item:item[1])
print("sorted list of tuple on the second element:",X)
X.sort(key=lambda item:item[1],reverse=True)
print("sorted list of tuple on the second element in reverse order:",X)
# # BASED ON last ELEMENT
X.sort(key=lambda item:item[1])
print("sorted list of tuple on the second element:",X)
X.sort(key=lambda item:item[1],reverse=True)
print("sorted list of tuple on the second element in reverse order:",X)
