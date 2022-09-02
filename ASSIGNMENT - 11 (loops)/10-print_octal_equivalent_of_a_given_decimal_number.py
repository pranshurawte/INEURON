n = int(input("enter a number : "))
a =''
while(n>0):
    a = str(a)+str(n%8)
    n //= 8

print(a)
