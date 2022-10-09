# Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class
import Calculator2
import Phone_class

class SmartPhone(Calculator2.Calculator2,Phone_class.Phone):
    pass

obj1 = SmartPhone()
obj1.msg()
