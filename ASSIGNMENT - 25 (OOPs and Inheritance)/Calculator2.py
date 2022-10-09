#Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.
class Calculator:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def subtract(x,y):
        return x - y

class Calculator2(Calculator):
    @staticmethod
    def mul(x,y):
        return x*y
    @staticmethod
    def div(x,y):
        return x / y

obj1 = Calculator2()
# print(obj1.add(4,3))
# print(obj1.subtract(4,3))
# print(obj1.mul(4,3))
# print(obj1.div(4,3))
