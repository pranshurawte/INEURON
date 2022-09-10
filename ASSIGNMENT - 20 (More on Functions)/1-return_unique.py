# Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique(l1) :
    s1 = set(l1)
    l2 = list(s1)
    return l2




new_list = unique([1,1,2,2,3,3,4,4,5,5])
print(new_list)
