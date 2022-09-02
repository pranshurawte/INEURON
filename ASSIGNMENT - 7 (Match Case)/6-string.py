# '''Write a python program to check whether a given string is a multiword string or single
# word string using match case statement'''

s = input("Enter any string : ")
s = s.split() #trims the spaces before and after the string
match s :
    case s if " " in s:
        print("Multi Word String") 
    case s if " " not in s :
        print("Single Word String") 
