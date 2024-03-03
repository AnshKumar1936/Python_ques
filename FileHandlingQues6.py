with open("Python\FilePractise.txt" , "r") as f:
    data=f.read()

new_data= data.replace("java" , "Python")
print(new_data)

with open("Python\FilePractise.txt" , "w") as f:
    data=f.write(new_data)
