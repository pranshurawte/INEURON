# Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not.


def co_prime_check(func) :
    def inner_function(num1,num2) :
        #making a list containing all the factors of num1 other than 1
        factors_of_num1 = []
        for i in range(2, num1) :
            if num1 % i == 0 :
                factors_of_num1.append(i)

        #making a list containing all the factors of num2 other than 1
        factors_of_num2 = []
        for i in range(2, num2) :
            if num2 % i == 0 :
                factors_of_num2.append(i)

        #factor checking    
        for ele in factors_of_num1 :
            if ele in factors_of_num2 :
                print("Not Co-Prime Numbers")
                func(num1,num2) 
            else :
                print("Co-Prime Numbers") 
    return inner_function 
            
@co_prime_check
def calculate_HCF(a,b) :
    #this fucntion is implemented by the help of Rakhi madam Aptitude logic 
    if a > b :
        term = b
    else :
        term  = a    
    while True :
        if a % term == 0 and b % term == 0 :
            print(term)
            break
        else :
            term = term - 1

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
calculate_HCF(a,b)
