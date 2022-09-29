#Create a generator to produce squares of first N natural numbers
def square_generator(n) :
    x = 1
    while n :
        yield x*x
        x = x + 1
        n = n - 1


for ele in square_generator(int(input("Enter a Number : "))) :
    print(ele , end= " ")
    