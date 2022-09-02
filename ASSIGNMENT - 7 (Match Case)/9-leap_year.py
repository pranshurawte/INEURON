# Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year

num = int(input("Enter a Number : "))

match num :
    case num if num % 400 != 0 :
        print("Non Century Leap Year")
    case num if num % 400 == 0 :
        print("Century Leap Year")
    case num if num % 400 != 0 and num % 4 == 0:
        print("Non Century Non Leap Year")
    case num if num % 400 == 0 and num % 4 == 0:
        print("Century Leap Year")