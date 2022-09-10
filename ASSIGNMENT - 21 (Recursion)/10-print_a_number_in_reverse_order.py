# Write a recursive python function to print a number in reverse order.

def reverse(num) :
    if num > 0 :
        print(num % 10)
        reverse( num // 10 )


reverse(int(input("Enter a number : ")) )    
