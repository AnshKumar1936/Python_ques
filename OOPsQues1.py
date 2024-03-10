class student:
    def __init__(self , name ,marks):
        self.name = name
        self.marks =  marks

    def get_avg(self):
        sum=0
        for i in self.marks:
            sum +=i
        print("Hi", self.name, "your avg score is" ,  sum/3)
    @staticmethod 
    def hello():
        print("hello")


s1=student("Ansh" , [99,67,88])
s1.get_avg()

s1.name = "Anmol"
s1.get_avg()

s1.hello()