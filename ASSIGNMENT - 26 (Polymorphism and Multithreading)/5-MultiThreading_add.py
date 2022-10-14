# Write a python script to create 2 threads to add all the values from 1 to 100.

from threading import *
from time import sleep
class A(Thread):
    def run(self):
        sum = 0
        for i in range(1,101):
            sum = sum + i
        # sleep(1)
        print(sum , "A ")
class B(Thread):
    def run(self):
        sum = 0
        for i in range(1,101):
            sum = sum + i
        # sleep(1)
        print(sum , "B ")

obj1 = A()
obj2 = B()

obj1.start()
obj2.start()

