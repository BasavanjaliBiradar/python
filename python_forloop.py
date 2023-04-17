# write a code to print numbers from 1 to 10
for num in range(1,11):# range(1,11) creates a list here[1,2,3,4,5,6,7,8,9,10]
    print(num)

# Write a code to print numbers from 1 to 10 using 2 steps or
# example to print odd numbefrs starting from value 1 
for num in range(1,11,2):
    print(num) #1 3 5 7 9 output

# Write a program to print numbers from 10 to 1 or reverse numbering
for num in range(10,0,-1):
    print(num) #10 9 8 7 6 5 4 3 2 1

# Write a program to calculate the sum of given list elements using for loop
# output=25
int_list =[4,8,-2,10,5]
list_sum=0
for num in int_list:
    list_sum=list_sum+num
print("Total sum of elements in list is :",list_sum)

# 0  + 4 = 4
# 4 + 8 = 12
# 12 + (-2) = 10
# 10 + 10 = 20
# 20 + 5 = 25
