# Write a python program to create a function to check whether a string is an anagram or not.

def anagram_check(s1,s2) :
    for i in s1 :
        if i not in s2 :
            print("Not Anagram Strings")
            break
    else :
        print("Anagram Strings")    



anagram_check(input("Enter 1st String : ") , input("Enter 2nd String : "))