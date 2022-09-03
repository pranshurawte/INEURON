# Write a python script to print first N even natural numbers

n = int(input("Enter a Number : "))
n = n * 2
i = 1
while i <= n : 
    if i % 2 == 0 :
        print(i , end = " ")
    i += 1    