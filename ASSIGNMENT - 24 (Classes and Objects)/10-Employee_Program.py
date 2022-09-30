# Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables. Also define instance methods to input fields and display field values

from unicodedata import name


class Employee :

    def __init__(self) :
        empid = 1
        name = "Pranshu"
        salary = 6000

    def initialize(self , empid , name , salary) :
        self.name = name
        self.empid = empid
        self.salary = salary
    
    def display(self) :
        print(self.empid,self.name,self.salary,sep = "\n")

emp1 = Employee()
emp1.initialize(39,"Betu",69000)
emp1.display()
