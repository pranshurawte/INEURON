# Write a recursive python function to calculate sum of first N even natural numbers

def sum(num ) :
    if num == 1 :
        return 2 
    return 2*num + sum(num - 1)    



print(sum(int(input("Enter a Number : "))))    