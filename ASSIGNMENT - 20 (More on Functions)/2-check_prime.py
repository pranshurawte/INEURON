# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def check_prime (num) :
    for i in range(2 , num) :
        if num % i == 0 :
            print("Not a prime Number ")
            break
    else :
        print("Prime Number")        


check_prime(int(input("Enter : ")))