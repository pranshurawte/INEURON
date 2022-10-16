# Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exceptions.
import math
a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))

try :
    print("Addition :", a + b)
    print("Subtraction: ", a - b)
    print("Multiplication" ,a * b)
    print("Division",a / b)
    print("Square Root" , math.sqrt(a))


except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You can not get take the square root of a negative number")

