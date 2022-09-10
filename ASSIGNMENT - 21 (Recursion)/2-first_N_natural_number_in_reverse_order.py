# Write a recursive python function to print first N natural numbers in reverse order

def printN(num) :
    if num > 0 :
        print(num)
        printN(num - 1)


printN(int(input("Enter a number : ")))    
