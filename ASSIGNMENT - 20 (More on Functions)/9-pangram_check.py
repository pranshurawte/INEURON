# Write a python program to create a function to check whether a string is a pangram or not.

def pangram_check(s1) :
    for i in range(97,123) :
        if chr(i) not in s1 :
            print("Not a Pangram String")
            break
    else :
        print("Pangram string")    

pangram_check(input("Enter in lower case : "))