# Write a python script to join 2 threads after printing completing the first Question.
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