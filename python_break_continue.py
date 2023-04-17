# How to use break statement
int_list=[1,5,7,8,19,13,17,3]

# Find the even value in the given list 
for num in int_list:
    print("current elements of the list:", num)
    if num%2==0:
        print("even number in the list:", num)
        break

# what if break is not given then unneccessory running/processed of remaining elements  
for num in int_list:
    print("current elements of the list:", num)
    if num%2==0:
        print("even number in the list:", num)
       
# How to use continue keyword?
# print the numbers from for loop and start them from value 1 but print vales on terminal if number is greater than 10
for num in range(1,21):
    if num < 10:
        continue
    print(num)

# if continue is not given
for num in range(1,21):
    if num < 10:
        print(num)# output = 1 2 3 4 5 6 7  8 9 
