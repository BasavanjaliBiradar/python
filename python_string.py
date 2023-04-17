# Create a string in python
str1 = "Anjali Biradar"
print(str1)
str2 = "Vivek's wife"
print(str2)
str3 = 'He is so "Handsome" man' # highlight handsome word in output in double qotes
print(str3)

# use string length fumction
print("length of the string:", len(str3))

# How to write a multi line string 
str4 = '''Anjali is 
not going 
to attend 
the function'''
print(str4)

#string concatination
str5 = "Anjali"
str6 = "Biradar"
print(str5+str6)

# string comparition
str7 = "Vivek"
str8 = "Vivek"
print(str7==str8)

# How to print the each caracter of the string i.e string slicing
for char in str7:
    print(char)

print(str7[0])
print(str7[1])
print(str7[2])
print(str7[3]) 
print(str7[4]) # it exactly works like a list

# # Update the  4th character in the string by U
# str7[3] = 'u'#'str' object does not support item assignment error we cannot update 
# print(str7)

str9 = "SOUMYA PATIL"

# convert string into lower case
print(str9.lower()) #soumya patil
# convert string into upper case
print(str9.upper()) # SOUMYA PATIL

# other functionalities will be same as list like slicing etc

# concatinating characters of the string one by one
str10 ="Anjali"
str11 = "Vivek"

#o/p = AVnijvaelki

for i in range(len(str10)):
    for j in range(len(str11)):
        if(i == j):
            print(str10[i]+str11[j]) #AV ni jv ae lk
