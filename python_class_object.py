#  how to create a class in python without any attributes
# class employe:# class which do not occupy any memory in this 
#     # contructer of the class needed to initialize anything in the class
#     def ___int___(self): #self keyword is a pointer to each object like call your own function
#         # instance attributes or instance values
#         self.emp_name= None #instance variable
#         self.emp_salary=None #none in python is no value in it it means

#     # METHOD OF A CLASS
#     def displayemployeinfo(self):
#         print("employe name:",self.emp_name,",employe salary:",self.emp_salary)

# emp1=employe()# object# once the object is created then the memory is occpied
# emp2=employe()# object # no error no output as no attributes passed in the class and object

class employee:
    # contructer of the class also act as a function def inside a class which will accept the user inputs 
    #constructer is mainly used for assignment of instance variables
    def __init__(self, name, salary):
        # instance attributes or instance values
        self.emp_name=name
        self.emp_salary=salary

        # Method of a class
    def displayemployeeinfo(self):
        print("employee name:",self.emp_name,",employee salary:",self.emp_salary)

emp1=employee('Anjali',10000)# object
emp2=employee('vivek',5000)# object

# print(emp1.displayemployeeinfo())#employee name: Anjali ,employee salary: 10000
# # None
# print(emp2.displayemployeeinfo())# # employee name: vivek ,employee salary: 5000
# # None

emp1.displayemployeeinfo() #employee name: Anjali ,employee salary: 10000
emp2.displayemployeeinfo() #employee name: vivek ,employee salary: 5000

print(emp1.emp_name)#Anjali # but these are not a right way to work with classes,attributes,instances
print(emp1.emp_salary)#10000
