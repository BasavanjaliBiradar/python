# Syntax
# while exp:
#     statements

# Write a program to print the table of 9
num = 9
counter = 1
while counter <=10:# Either True or False
    ans=num * counter
    print(num,'*',counter,'=',ans)
    counter=counter+1

# what will happen if counter is not incremented this will stuck in a infinite loop of 9*1=9 i.e stack overflow may lead to stackoverflow error 
num = 9
counter = 1
while counter <=10:# Either True or False
    ans=num * counter
    print(num,'*',counter,'=',ans)

# What will happen? leads to infinite loop bez no condituional check ,explicitly mentioned bool True 
while True:
    print("Anjali")
