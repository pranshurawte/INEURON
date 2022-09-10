# Write a recursive python function to print first N natural numbers.

def first_N_nat_no(num) :
    if num > 0 :
        first_N_nat_no(num - 1)
        print(num)


first_N_nat_no(int(input("Enter a number : ")))    
