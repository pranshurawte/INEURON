# Write a python script to create 5 threads to fill a list with random numbers till 100.
from time import sleep
from threading import *
import random
class A(Thread) :
    def run(self):
        l1.append(random.randrange(1,101))
class B(Thread) :
    def run(self):
        l1.append(random.randrange(1,101))
class C(Thread) :
    def run(self):
        l1.append(random.randrange(1,101))
class D(Thread) :
    def run(self):
        l1.append(random.randrange(1,101))
class E(Thread) :
    def run(self):
        l1.append(random.randrange(1,101))

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()
obj5 = E()
l1 = []
obj1.start()
obj2.start()
obj3.start()
obj4.start()
obj5.start()
print(l1)
