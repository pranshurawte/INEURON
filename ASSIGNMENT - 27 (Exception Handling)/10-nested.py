# Write a python script to implemented a nested Try Except block
a = 6 
b = int(input("Enter a number :"))
c = 0
try:
    c = a / b

except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Enter a number.")
        

