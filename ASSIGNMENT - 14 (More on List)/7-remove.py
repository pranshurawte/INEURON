# Write a Python script to remove all non int values from a list.
l1 = [" hello " , 34 , 39.6 , 3 + 4j  , 69 ]
print(l1)
i = 1
while i < 5 :
    if l1[i] == int :
        l1 = l1.remove(l1[i])
    i += 1    
print(l1)        
