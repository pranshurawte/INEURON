# Write a python script to find next prime number of a given number

n = int(input("Enter a number : "))

for var in range(n, n*2) :
    for ele in range(2 , var) :
        if var % ele == 0 :
            break
    if var % ele != 0 :
        print(var , end = " ") 
        break   