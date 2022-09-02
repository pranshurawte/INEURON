# Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. User can answer in a sentence like “I like red colour”. Assuming all colour name entered by user is in lowercase. Use match case to display day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday

s = input("Enter your favourite color : ")

match s :
    case string if "yellow" in s :
        print("Monday")
    case string if "blue" in s :
        print("Tuesday")
    case string if "orange" in s :
        print("Wednesday")
    case string if "white" in s :
        print("Thursday")
    case string if "black" in s :
        print("Friday")
    case string if "red" in s :
        print("Saturday")
    case _ :
        print("Sunday")