# Write a recursive python function to calculate sum of squares of first N natural numbers

def square_sum(num) :
    if num == 1 :
        return 1
    return num*num + square_sum(num - 1)    



print(square_sum(int(input("Enter a Number : "))))    
