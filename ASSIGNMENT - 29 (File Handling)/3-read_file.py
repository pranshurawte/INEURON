# Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

f = open("file1.txt","r")
content = f.read()
print(content)
f.close()