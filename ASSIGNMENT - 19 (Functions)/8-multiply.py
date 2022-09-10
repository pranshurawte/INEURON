# Write a python program to multiply all the numbers in a list.

def multiply (l1) :
    product = 1
    for i in l1 :
        product *= i
    return product    


product = multiply([5,6,10])
print(product)