class Car:
    def __init__(self , type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("car is stopped")

class Toyota(Car):
    def __init__(self, name , type):
        super().__init__(type)
        self.name=name
        super().start()

car1= Toyota("Fortuner" , "Diesel")
print(car1.name)
print(car1.type)