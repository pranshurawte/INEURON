#Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
l1 = [5,9,7,3]
l2 = [1,2,3,4]

d1 = {}
i = 0 
while i < 4 :
    d1[l2[i]] =l1[i]
    i += 1
    
print(d1)

