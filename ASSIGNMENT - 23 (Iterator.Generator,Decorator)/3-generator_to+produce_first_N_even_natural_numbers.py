#Create a generator to produce first n even natural numbers
def even_generator(n) : 
    x = 2
    while n :
        n = n - 1
        yield x 
        x = x + 2

for ele in even_generator(int(input("Enter a Number : "))) :
    print(ele , end = " ")
