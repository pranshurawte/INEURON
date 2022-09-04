# Write a python script to check whether a given number is Prime or not
n = int(input("Enter a Number  : "))
bool = True

for ele in range(2,n) : 
    if n % ele == 0 :
        print("Not a Prime Number ")
        bool = False
        break

if bool == True :
    print("Prime Number")   




# # Write a python script to check whether a given number is Prime or not
# n = int(input("Enter a Number  : "))
# bool = True
# i = 2
# while i < n :
#     if n % i == 0 :
#         print("Not a Prime Number  ")
#         bool = False
#         break
#     i += 1

# if  bool == True :
#     print("Prime Number")


