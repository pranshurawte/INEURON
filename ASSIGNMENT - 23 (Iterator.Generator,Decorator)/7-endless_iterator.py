# Create an endless iterator using generator method to produce terms of Fibonacci series

def fib() :
    a,b = 0,1
    while True :
        yield a
        a,b = b,a+b

it = fib()
fib_list = []
while True:
    ans = input("Do you want to print the next element ?(y/n) : ")  
    if ans == 'y' :
        x = next(it)
        print(x)
        fib_list.append(x)
    else :
        print(fib_list)
        break    



