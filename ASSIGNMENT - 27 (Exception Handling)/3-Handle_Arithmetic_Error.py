# Write a python script to handle the ArithmeticError
from nntplib import ArticleInfo


a = 6 
b = int(input("Enter a Number"))
try:
    if a==b:
        raise ArithmeticError()
except ArithmeticError:
    print("Arithmetic Error")