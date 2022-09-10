# Write a recursive python function to print first N even natural numbers.

def firstN(num) :
    if num > 0 :
        firstN( num - 1)
        if num % 2 == 0 :
            print( num )



firstN(int( input("Enter a number : ")) * 2 )    
