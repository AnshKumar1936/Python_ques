def show(n):
    if(n==0):
       return
    print(n)
    show(n-1)
    print("OK")
    print("DONE")

show(3)