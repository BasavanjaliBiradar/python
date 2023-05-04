# exception handling
a=5
try:
    result=a/2
except ZeroDivisionError:
    print("error occured bez of division by 0")
else:
    print("calculation completed")
    print(result)
    
b=2
try:
    result=a/1
except ZeroDivisionError:
    print("error occured bez of division by 0")
else:
    print("calculation completed")
    print(result)
finally:
    print("doent matter try-except but i will print myself")#database connection close
