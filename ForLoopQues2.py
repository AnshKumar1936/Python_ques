tup=(1,2,9,16,25,36,49,64,81,100)
x=100
idx=0
for i in tup:
    if(i==x):
        print("Found at idx", idx)
        break
    idx+=1
else:
     print("Not Found")
    