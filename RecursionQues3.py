def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list , idx+1)

fruits = ["Apple" , "Mango" , "Litchi" , "Guava"]

print_list(fruits)