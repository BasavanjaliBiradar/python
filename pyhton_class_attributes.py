# difference between class variable and instance variable 
# class attribute is the global kind of variable works for all objects in the class 
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
emp2=employee('vivek',5000)# object
emp1.displayemployeeinfo()#employee name: Anjali ,employee salary: 10000
emp1.displayemployeecount()#employee count: 2
emp2.displayemployeeinfo()#employee name: vivek ,employee salary: 5000
emp2.displayemployeecount()#employee count: 2
