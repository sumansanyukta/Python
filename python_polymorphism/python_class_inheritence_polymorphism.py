# Create a class called Vehicle and make car, boat, plane child classes of vehicle:

class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("sail!")

class plane(vehicle):
    def move(self):
        print("fly!")

car1 = car("Ford", "Mustang")
boat1 = boat("ibize", "tour20")
plane1 = plane("boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()