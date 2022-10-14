#Write a python script to create a to print the above user account object using operator overloading (hint __str__ method).

class UserAccount :
    def __init__(self,user_id,balance):
        self.user_id = user_id
        self.balance = balance
    def __add__(self,user2):
        total_userid = self.user_id + user2.user_id 
        total_balance = self.balance + user2.balance 
        user4clear = UserAccount(total_userid,total_balance)
        return user4clear
    def __str__(self) :
        return str(self.user_id)  + " " + str(self.balance)

user1 = UserAccount(1,100)
user2 = UserAccount(2,200)
user3 = UserAccount(3,300)
new_user = user1 + user2 
new_user2 = new_user + user3
print(user1)
print(user2)
print(user3)
print(new_user2)
