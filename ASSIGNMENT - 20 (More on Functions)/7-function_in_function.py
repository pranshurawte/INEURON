# Write a python program to access a function inside a function.

def f2() :
    print("Function inside Function")


def f1() :
    f2()

f1()