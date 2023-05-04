# how to handle exceptions in python?
# a=10
# print("hello!!!")#printed output as hello!!!
# print(a/0) #ZeroDivisionError: division by zero ./exception
# print("bye!!!")# not printed as the error is poped and entire code stoped working
# #  therefore we need exception handling in programing

# list_a=[2,6,8,1,30]
# print(list_a[7])#IndexError: list index out of range

a=5
try:
    # mysql.connect(host,user,pswd,authentication)# connect with database 
    result=a/0
    print(result)
except:
    print("some error has occured!!!")#some error has occured!!!

print("bye!!!")#bye!!! no haulted even after exception bez we have handled the exception

# in python around 30-40 exceptions are defined there r 2 ways to deal with them 
num =5
list_a=[1,2,3,4,7,90,20]
dic_a={'Anjali':25,'vivek':30}
try:
    print("divide number by zero")#divide number by zero
    result=num/0# if its fixed the value as 5 then all the bellow 2 print statements will be printed
    print("step one done!!!")
    print(result)

    print("access 11th element of the list")
    print(list_a[11])# if given list_a[5] then the lines below print statements get printed
    print("step two done!!!")

    print("access value of the appu from dictionary")
    print(dict_a['appu'])# key error 
    print("step three done!!!")
# except:
    # print("some error has been occured")#some error has been occured

# keyerror,ioerror,indexoutofrange,zerodivisionerror
except ZeroDivisionError:
    print("this error was occured bez division by zero happend")
except IndexError:
    print("this error was occured bez index is out range")
except KeyError:
    print("this error was occured bez search key doesnt exist")

#one tryblock and multiple except can be written but it will execute one except method at one time 

except Exception as err:#Exception keyword can handle all kind of defined exceptions in python /error in python
    print("error occured and message :",err)
