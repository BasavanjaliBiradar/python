class employee:
    # class variable or attribute/normal variable/global
    empcount=0

    # contructer of the class 
    def __init__(self, name, salary):
        # instance attributes or instance values
        self.emp_name=name
        self.emp_salary=salary
        employee.empcount+=1
        # Method of a class
    def displayemployeeinfo(self):
        print("employee name:",self.emp_name,",employee salary:",self.emp_salary)
         # Method of a class
    def displayemployeecount(self):
        print("employee count:",employee.empcount)

emp1=employee('Anjali',10000)# object
emp1.displayemployeeinfo()#employee name: Anjali ,employee salary: 10000
emp1.displayemployeecount()#employee count: 2


emp2=employee('vivek',5000)# object
emp2.displayemployeeinfo()#employee name: vivek ,employee salary: 5000
emp2.displayemployeecount()#employee count: 2

# print instance variable of a object
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp2.emp_name)
print(emp2.emp_salary)

# lets axcess class variable from instance itself
print(emp1.empcount)
print(emp2.empcount)

# can change these values and axcess using instances
emp1.empcount=10
emp2.empcount=20 #value not over writen the scope of the value assigned is limited to for that instance only not other instances of that class
print(emp1.empcount)#10
print(emp2.empcount)#20

print(employee.empcount) #2

# what is the static method in python?
# static methods tightly coupled with the class itself 
# no object creation to be called in static method
class car:
    def __init__(self,name,color):
        self.car_name=name
        self.car_color=color
    def displaycardetails(self):
        print("Car name is ",self.car_name,"and Car color is ",self.car_color)

    @staticmethod
    def initialMessage():
        print("welcome to Anjali showroom!!!")

# print(car.displaycardetails())# error bez no object created
car.initialMessage()#welcome to Anjali showroom!!!--> called using class reference , no need to create a object for a static methods
car1=car('XUV 700','Red')
car1.displaycardetails()#Car name is  XUV 700 and Car color is  Red

# car.displaydetails()# error will not work without object

class employee:
    @staticmethod
    def isemployeeof():
        print("Iam an employee of Apple!!")

employee.isemployeeof()#Iam an employee of Apple!!

class calculation:
    @staticmethod
    def addtwonums(num1,num2):
        print("sum of two numbers=",num1+num2)
calculation.addtwonums(10,5)#sum of two numbers= 15
