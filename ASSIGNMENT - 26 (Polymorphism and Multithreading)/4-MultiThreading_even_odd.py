#Write a python script to create two Threads. First thread will print all Even numbers and Second thread will print all Odd numbers till 100.

from threading import *
from time import sleep

class Even(Thread):
    def run(self):
        for i in range(1,101):
            if i % 2 == 0:
                print(i)
                sleep(1)

class Odd(Thread):
    def run(self):
        for i in range(1,101):
            if i % 2 == 1:
                print(i)
                sleep(1)

obj1 = Even()
obj2 = Odd()
obj1.start()
obj2.start() 




        