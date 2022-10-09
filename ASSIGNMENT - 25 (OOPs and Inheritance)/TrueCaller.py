# Write a python script to create an application like Truecaller where names and numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).

class Truecaller():
    def __init__(self,name,number):
        self.name = name
        self.number = number
        call_directory[name] = number
    def fetch_name(self):
        print(self.name)

call_directory = {}
obj1 = Truecaller("Pranshu",6261293988)
obj2 = Truecaller("Dad",8109492670)
print(call_directory)
