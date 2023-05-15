#N largest element in list
l=list(input("enter the elements of the list space saperated:").split(" "))#25 67 90 89 789
n=int(input("enter the elements number of larger values you need from the list:"))#3
l.sort()
print(l[-n:])#['789', '89', '90']
