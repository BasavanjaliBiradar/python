str=input("please enter the string:")#anjali
ch=input("please enter the character to be removed:")#a
print(str.replace(ch,""))# nj li

# remove i'th element from a string USING REPLACE METHOD
def removech(s1,s2):
    print(s1.replace(s2," "))
s1=input("please give a string :")
s2=input("please enter the character to be removed:")
removech(s1,s2)
