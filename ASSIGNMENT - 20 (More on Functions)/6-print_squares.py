# Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def print_square() :
    l1 =  [ i**2 for i in range(1,31)]
    print(l1)

print_square()  