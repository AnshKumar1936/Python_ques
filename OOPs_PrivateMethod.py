class Person:
    __name= "Ansh"

    def __hello(self):
        print("HELLO GUYS")


    def welcome(self):
        self.__hello()
        print("Welcome Called")

  

p1=Person()
print(p1.welcome())
