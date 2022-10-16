# Write a python script to handle multiple Exception in one try

a = 6 
b = int(input("Enter a number :"))
c = 0
try:
    c = a / b
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Enter a number.")

