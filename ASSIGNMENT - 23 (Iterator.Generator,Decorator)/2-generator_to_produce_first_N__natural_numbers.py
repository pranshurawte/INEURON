#Create a generator to produce first n odd natural numbers
def odd_generator(n) :
    x = 1
    while n :
        yield x
        x = x + 2
        n = n - 1 

for ele in odd_generator(int(input("Enter a Number : "))) :
    print(ele, end = " ")
