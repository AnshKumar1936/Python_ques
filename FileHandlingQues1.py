f=open("Python\FileHandling.txt" , "r")

data=f.read(18)
print(data)

file1=f.readline()
print(file1)

file2=f.readline()
print(file2)
f.close()
