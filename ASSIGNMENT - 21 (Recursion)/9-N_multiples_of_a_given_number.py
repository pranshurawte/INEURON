# Write a recursive python function to print first N multiples of a given number.

def multiples(num ) :
    if num > 0 :
        multiples( num - 1)
        print( num * 10 )




multiples(int(input("Enter a number : ")))    
