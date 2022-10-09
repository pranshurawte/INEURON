# Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
class Calculator:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def subtract(x,y):
        return x - y

print(Calculator.add(4,3))
print(Calculator.subtract(4,3))