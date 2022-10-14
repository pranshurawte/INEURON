# Write a python script to check whether a given number is prime or armstrong number using 2 different threads.
from threading import *
from time import sleep

class Prime(Thread):
    def __init__(self,number):
        self.number = number

    def run(self):
        for i in range(2,self.number):
            if self.number % i == 0 :
                print("Not a Prime Number")
                break
        else :
            print("Prime Number")
        
class Armstrong(Thread):
    def __init__(self,number):
        self.number = number
    def run(self):
        length = len(self.number)
        int_num = int(self.number)
        sum = 0
        for i in range(length):
            digit = int_num % 10
            sum = sum + digit*digit
            int_num = int_num // 10
        if sum == int_num :
            print("Armstrong Number")
        else :
            print("Not a Armstrong Number")  
    

num = int(input("Enter a Number : "))
obj1 = Prime(num)
obj2 = Armstrong(str(num))
obj1.start()
obj2.start()

  