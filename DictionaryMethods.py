dict={
    "name" : "Ansh kumar singh",
    "course" : "BCA", 
    "section" : "C1"
}

print(list(dict.keys()))
print(len(dict))
print(list(dict.values()))

print(list(dict.items()))


print(dict["name"])
print(dict.get("name"))

dict.update({"city" : "Dehradun" , "age" : "19"})

print(dict)