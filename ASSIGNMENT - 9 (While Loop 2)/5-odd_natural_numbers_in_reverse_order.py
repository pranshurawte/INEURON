# Write a python script to print first N odd natural numbers in reverse order
n = int(input("Enter a Number : ")) 
n = n * 2
while n > 0 :
    if n % 2 != 0 :
        print(n ,end = " ")
    n -= 1    