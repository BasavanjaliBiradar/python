# Numerical operations in python
# + for addition
# - for substraction
# * for multipication
# / for float division
# // for integer dividion
# ** for power calculation
# % for modulus

x = 5
y = 3
print("Addition of x+y=", x+y)
print("Substraction of x-y=", x-y)
print("Multiplication of x*y=", x*y)
print("Float Division of x/y=", x/y)
print("Integer Division of x//y=", x//y)
print("Power of x**y=", x**y)
print("Modulus of x%y=", x%y)

# Some operations on string in python
str_name = "Anju"
empty_str =""
# concat operation for string in python
Full_Name = str_name + " " +"Biradar"
print(Full_Name)

# if we can use - as well? it will not work
    #minus_str ="Anju"-"Biradar"#unsupported operater error
    #print(minus_str)
    #mul_str ="Anju"*"Biradar"#unsupported operater error
    #print(mul_str)
    #power_str ="Anju"**"Biradar"#unsupported operater error
    #print(power_str)
    #p_str ="Anju"**3 #unsupported operater error but it works in python 2 version not wrking in py 3 //output-AnjuAnjuAnju
    #print(p_str)
mult_numeric_str ="Anju"*3 
print(mult_numeric_str)

#assignment operators in python
# = assignment operator ex: x=5
# += , x+=5-->x=x+5
# -= , x-=5-->x=x-5
# *=, x*=5-->x=x*5
# /=, x/=5-->x=x/5
# //=, x//=5-->x=x//5
# %=, x%=5-->x=x%5

#comparision operators in python (we compare our operand values)
# ==, equals to condition ex: x==y
# !=, not equals to condition ex:x!=y
# >=,greater than and equals to condition ex:x>=y
# <=,lesser than and equals to condition ex:x<=y
# >, greater than or not condition ex x>y
# <, lesser than or not condition ex x<y

a=10
b=5
print("result of x==y:", x==y)
print("result of x!=y:", x!=y)
print("result of x>y:", x>y)
print("result of x<y:", x<y)
print("result of x>=y:", x>=y)
print("result of x<=y:", x<=y)

#logical operations in python (logical chech will happen for expression rtesult)
# and -> ReturnS True if both the statements are True
# or -> ReturnS True if one of the statements are True
# not -> Reverse the result,ReturnS False if result is True
m = 10
n = 8
print("m>10 and n<10 Result:",m>10 and n<10) #false and true= false
print("m>20 or n<10 Result:",m>20 or n<10) #false and true= true
print("m>20 not n<10 Result:",not(m>20 and n<10)) # not(false and true)= not(false)=true

# computing the sum of even numbers
sum = 0
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
 if i % 2 == 0:
   sum = sum + i
print("sum =",sum)
