class A:
    var1= "This is A class"

class B:
    var2= "This is B class"

class C(A,B):
    var3= "This is C class"


c1 = C()
print(c1.var1)
print(c1.var2)
print(c1.var3)