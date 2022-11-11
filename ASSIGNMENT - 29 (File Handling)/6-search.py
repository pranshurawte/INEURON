# Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not
def search(search_word):
    for line in f.readlines():
        strlist = line.split(" ")
        for word in strlist :
            if word == search_word :
                return word
    else :
        return None
f = open("cities.txt","r")
search_word = input("Enter a city name :")
print(search(search_word))

f.close()