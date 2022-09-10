# Write a recursive python function to print first N odd natural numbers in reverse order

def firstN(num) :
    if num > 0 :
        if num % 2 == 1 :
            print(num)
        firstN( num - 1)    


firstN(int(input("Enter a number : ")) * 2)    
