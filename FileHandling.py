f = open("Python\FileHandling.txt" , "r")

data=f.read()
print(data)
print(type(data))
f.close()