class Vehicle:
    def fuel_type(self):
        print("Most vehicles use petrol or diesel")

class Car(Vehicle):
    def wheels(self):
        print("A car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("A bike has 2 wheels")

car = Car()
bike = Bike()

print("Car Details:")
car.fuel_type()  
car.wheels()     

print("\nBike Details:")
bike.fuel_type() 
bike.wheels()    
