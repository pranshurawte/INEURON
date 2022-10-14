#Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.

class Apple:
    def multiply(self,a,b = None,c = None):
        if b == None :
            return a
        elif c == None :
            return a*b
        else :
            return a*b*c


obj1 = Apple()
print(obj1.multiply(2))
print(obj1.multiply(2,3))
print(obj1.multiply(2,3,4))