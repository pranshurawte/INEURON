# Write a python program to check whether a given number is positive, negative or zero using match case statement

num = int(input("Enter a Number : "))

match num :
    case num if num == 0 :
        print("Zero")
    case num if num < 0 :
        print("Negative")
    case num if num > 0 :
        print("Positive")