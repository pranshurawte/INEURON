# Write a recursive python function to print first N even natural numbers in reverse order.

def firstN(num) :
    if num > 0 :
        if num % 2 == 0 :
            print( num )
        firstN( num - 1 )    
            


firstN(int( input("Enter a number : ")) * 2 )    
