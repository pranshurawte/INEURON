# Create a generator to produce first n prime numbers
# 2,3,4,5,7,11,13,17,19,23,
def prime(n) :
    for i in range(1,n+1):
        for j in range(2,i):
            if i % j == 0 :
                break
            else :
                n = n - 1
                yield i
                break


for ele in prime(int(input("Enter a Number : ")) * 2) :
    print(ele , end = " ")  
    