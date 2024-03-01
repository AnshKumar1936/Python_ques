f=open("Python\FileHandling.txt" , "w")

data=f.write("I am learning Python")

print(data)

f.close()

f=open("Python\FileHandling.txt" , "a")

data=f.write("\nthen i will do javascript")

print(data)
