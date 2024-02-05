marks= int(input("Enter the marks of student"))

if(marks>=90):
    print("YOU GOT GRADE A")
elif(marks<=90 and marks>=80):
    print("YOU GOT GRADE B")
elif(marks<=80 and marks>=70):
    print("YOU GOT GRADE C")
elif(marks>70 and marks<=60):
    print("YOU GOT GRADE D")
else:
    print("YOU GOT FAIL")
