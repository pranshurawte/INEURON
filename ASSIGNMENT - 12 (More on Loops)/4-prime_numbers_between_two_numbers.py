# Write a python script to print all Prime numbers between two given numbers (both values inclusive)
n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))

for var in range(n1 , n2) :
    for ele in range(2 , var) :
        if var % ele == 0 :
            break
    if var % ele != 0  :
        print(var , end = " ")