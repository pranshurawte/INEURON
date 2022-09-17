# Write a recursive python function to calculate the factorial of a number.

def fact( num ) :
    if num == 1 :
        return 1
    return num * fact(num - 1)


    
print(fact(int(input("Enter a Number : "))))    
