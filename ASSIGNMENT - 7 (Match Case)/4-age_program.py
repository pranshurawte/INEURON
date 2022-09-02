# Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen

category = int(input("Enter the age : "))

# if age < 10 :
#     category = 1 
# elif age < 20 :
#     category = 2 
# elif age < 40 :
#     category = 3 
# elif age < 60 :
#     category = 4
# else  :
#     category = 5


match category :
    case category if category in range(0,10):
        print("Kid")    
    case category if category in range(10,20) :
        print("Teen")    
    case category if category in range(20,40) :
        print("young")    
    case category if category in range(40,60) :
        print("Experienced")    
    case category if category in range(60,100) :
        print("Senior Citizen") 
    case _ :
        print("Invalid Entry")       
