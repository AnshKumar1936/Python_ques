class car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")


class Toyota(car):
    def __init__(self , brand):
        self.brand=brand

class fortuner(Toyota):
    def __init__(self, type):
        self.type=type


car1= fortuner("diesel")
car.start()