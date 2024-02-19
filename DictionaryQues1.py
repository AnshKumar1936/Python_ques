marks={}

x=int(input("enter physics marks:"))
marks.update({"physics" : x})
y=int(input("enter maths marks:"))
marks.update({"maths" : y})
z=int(input("enter chemistry marks:"))
marks.update({"chemistry" : z})

print(marks)