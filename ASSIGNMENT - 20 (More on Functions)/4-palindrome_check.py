# Write a python program to create a function that checks whether a passed string is palindrome or not.

def palindrome_check(s1) :
    if s1 == s1[::-1] :
        print("Palindrome String")
    else :
        print("Not a Palindrome")    
    

palindrome_check(input("Enter : "))