# Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def calculate(s1) : 
    count_upper = 0 
    count_lower = 0
    for i in s1 :
        if ord(i) in range(97,123) :
            count_lower += 1
        if ord(i) in range(65,91):
            count_upper += 1
    print("Lower Case count = ",count_lower ,"Upper Case count = ",count_upper )      

calculate(input("Enter : "))



