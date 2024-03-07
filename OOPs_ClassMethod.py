# class student:
#     @classmethod
#     def college(cls):
#         print("I am in year")

# std=student()
# print(std.college())


class person:
    name = "random"

    # def change_name(self ,  name):
    #     self.name = name

    @classmethod
    def change_name(cls , name):
        cls.name=name

p1=person()
p1.change_name("Ansh Kumar")
print(p1.name)
print(person.name)