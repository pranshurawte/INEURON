# Write a recursive python function to calculate sum of the digits of a given number

def sum_digit(num) :
    if num < 10 :
        return num
    new = num    
    return num % 10 + sum_digit( num // 10 )


print(sum_digit(int(input("Enter a Number : "))))    
