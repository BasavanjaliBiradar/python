# # Inheritance in python
# # aka parent class
# class person():
#     def __init__(self,name):
#         self.person_name=name
#     def displayname(self):
#         print("name of a person is ",self.person_name)
#     # by default we can say that particular person is unemployed
#     def isemplyed(self):
#         print(self.person_name,"is Un-employed!!")

# # derived class, aka child class
# class Employee(person):
#       def isemplyed(self):
#         print(self.person_name,"is employed!!") #IT IS LIKE OVERWITTING

# emp=person("Anjali")
# emp.displayname()
# emp.isemplyed()

# emp1=Employee("anjali")
# emp1.displayname()#name of a person is  anjali
# emp1.isemplyed()#anjali is employed!!

# how to initalize constructor of base class

# Inheritance in python
# base class aka parent class
class person():
    def __init__(self,name):
        self.person_name=name
    def displayname(self):
        print("name of a person is ",self.person_name)
    # by default we can say that particular person is unemployed
    def isemplyed(self):
        print(self.person_name,"is Un-employed!!")

# derived class, aka child class
class Employee(person):
    def __init__(self,emp_name,idno,salary,designation):
        self.idnumber=idno
        self.emp_salary=salary
        self.emp_designation=designation
        #calling constructor of base class
        person.__init__(self,emp_name)# not used this mthod in oops
        super().__init__(emp_name)#super class constructor

    def isemplyed(self):
        print(self.person_name,"is employed!!") #IT IS LIKE OVERWITTING
    def employeedetails(self):
        print("employe id is:",self.idnumber,"and employee salary is:",self.emp_salary,"and the employee designation is :",self.emp_designation)

emp=person("Anjali")
emp.displayname()
emp.isemplyed()
# emp.emp_salary# error
# emp.employeedetails()# error bez no employee details method in person class

# emp1=Employee("anjali")
# emp1.displayname()#name of a person is  anjali
# emp1.isemplyed()#anjali is employed!!
# emp1.name# acessable

emp1=Employee("Anjali",2890,1000000,"Dataengineer")
emp1.displayname()#name of a person is  Anjali
print(emp1.person_name)#AttributeError: 'Employee' object has no attribute 'name'# afterchanging name to person_name output is Anjali
emp1.employeedetails()#employe id is: 2890 and employee salary is: 1000000 and the employee designation is : Dataengineer
