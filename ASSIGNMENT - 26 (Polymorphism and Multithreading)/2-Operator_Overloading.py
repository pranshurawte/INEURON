#Write a python script to create a user account class with 2 instance variables (userid and balance). Create 3 user objects and add all the users using operator overloading.

class UserAccount :
    def __init__(self,user_id,balance):
        self.user_id = user_id
        self.balance = balance
    def __add__(self,user2):
        total_userid = self.user_id + user2.user_id 
        total_balance = self.balance + user2.balance 
        user4clear = UserAccount(total_userid,total_balance)
        return user4clear
        


user1 = UserAccount(1,100)
user2 = UserAccount(2,200)
user3 = UserAccount(3,300)
new_user = user1 + user2 
new_user2 = new_user + user3
print(new_user2.user_id)
print(new_user2.balance)
