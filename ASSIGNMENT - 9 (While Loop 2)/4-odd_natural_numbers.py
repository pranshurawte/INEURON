# Write a python script to print first N odd natural numbers
n = int(input("Enter a Number : "))
i = 1
while i < n*2:
    if i % 2 == 1 : 
        print(i,end = " ")
    i +=1