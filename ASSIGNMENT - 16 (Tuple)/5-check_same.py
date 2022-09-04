# Write a python program to check if all items in the tuple are the same.
t1 = ( 5,5,5,5,5,5,5)
t2 = (5,69,7,12,6)

i = 0 
while i < len(t1) - 1 :
    if t1[i] != t1[i + 1] :
        print("Not Same")
        break
    i += 1
else :
    print("Same")

i = 0 
while i < len(t2) - 1 :
    if t2[i] != t2[i + 1] :
        print("Not Same")
        break
    i += 1
else :
    print("Same")
