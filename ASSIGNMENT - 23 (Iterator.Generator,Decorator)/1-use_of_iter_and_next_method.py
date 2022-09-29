#Use iter and next method to access all the elements of a given set using while loop
s1 = {1,2,3,4,5,6,7,8}

it = iter(s1)
i = 0
while i < 8 :
    i=i+1
    print(next(it))