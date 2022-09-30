import random 

def number_generator():
    list_numbers_already_generated = []
    current_number = random.randrange(0,5)
    flag = True
    while True :
        if current_number in list_numbers_already_generated:
            current_number  = random.randrange(0,5)
        else :
            list_numbers_already_generated.append(current_number) 
            # flag = False
            return current_number
    


name = input("Enter your Name : ")
print("\nWelcome",name,"to the WORD PUZZLE GAME\n")
print("Rules :- \n")
print("1.You will be given 5 jumbled words , you have to solve one at a time.","2.You have to form the correct word out of a all given set of characters." ,"3.You will score +1 for each correct answer ","4.You will score -1 for each wrong answer.\n", sep = "\n")

list_of_jumbled_words = ["RAEHTF" ,"KABRE" ,"CYROTNU" , "RENEG" ,"OAERELANP"]
list_of_correct_words = ["father","brake","country","green" , "aeroplane"]
score = 0



for i in range(5):
    print("Your Jumbled Word is :- ")
    random_num_generated = number_generator()
    

    print(list_of_jumbled_words[random_num_generated])
    entered_answer = input("Enter your Answer : ")
    if entered_answer == list_of_correct_words[random_num_generated] :
        score +=1
    else :
        score -=1  
    print("\n")    

  
print("You scored",score,"out of 5.")
match score :
    case 0 :
        print("\nOOPS !! You need to work harder .")
    case 5 :
        print("\nHURRAH !! You are a Champion. ")   





