# Write a python script to update the above Profile class with encapsulation.

class Profile :
    def __init__(self,name,email,age) :
        self.name = name
        self.email = email
        self.age = age

    def show(self):
        print(self.name,self.email,self.age,sep = "\n")

P1 = Profile("Pranshu","kravate35@gmail.com",20)
print(P1.name)
print(P1.email)
print(P1.age)