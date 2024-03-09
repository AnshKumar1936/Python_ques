class car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")


class Toyota(car):
    def __init__(self , name):
        self.name=name

car1=Toyota("Fortuner")
car2=Toyota("Land cruiser")

print(car1.start())
print(car1.color)
print(car1.name)
print(car2.name)
print(car1.stop())