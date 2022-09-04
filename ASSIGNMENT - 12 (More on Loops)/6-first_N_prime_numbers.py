n = int(input("Enter a Number : "))
for var in range(3,n*10) :
    for ele in range(2 ,var) :
        if var % ele == 0 :
            break
    if var % ele != 0 :
        print(var, end = " ")
    