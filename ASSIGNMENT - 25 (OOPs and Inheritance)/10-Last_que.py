# Write a python script to add the new method in SmartPhone class which accepts Truecaller object as a parameter and call the fetch method of Truecaller.
import TrueCaller
class Calculator:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def subtract(x,y):
        return x - y

class Calculator2(Calculator):
    @staticmethod
    def mul(x,y):
        return x*y
    @staticmethod
    def div(x,y):
        return x / y

class Phone() :
    def calling(self) :
        print("Calling........")
    def msg(self):
        print("Messaging.......")

class SmartPhone(Calculator2,Phone):
    def adv_f(self,other):
        other.fetch_name()


t1 = TrueCaller.Truecaller("Meena Mumma",9826047488)
s1 = SmartPhone()
s1.adv_f(t1)
