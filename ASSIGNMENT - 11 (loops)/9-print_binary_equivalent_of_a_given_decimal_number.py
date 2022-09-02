# do not use bin() method
a = ''
num = int(input("Enter a Number : "))

while num > 0 :
    if num % 2 == 0 :  
        a += '0'
    else :    
        a+= '1'
    num //= 2

print(a[::-1])



    
