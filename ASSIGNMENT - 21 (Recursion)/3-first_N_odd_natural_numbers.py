# Write a recursive python function to print first N odd natural numbers

def firstN(num) :
    if num > 0 :
        firstN(num - 1)
        if num % 2 == 1 :
            print(num)


firstN(int(input("Enter a number : ")) * 2)    
