# Write a python script to update 2nd Question, change email and age to __email and __age.

class Profile :
    def __init__(self,name,email,age) :
        self.name = name
        self.__email = email
        self.__age = age

    def show(self):
        print(self.name,self.__email,self.__age,sep = "\n")
        #here writing double underscore makes the attribute private , so it can't be accessed outside the class without the help of the method
        

P1 = Profile("Pranshu","kravate35@gmail.com",20)
P1.show()
# this will give error as it is not accessebile like this :-
# print(P1.__age)

