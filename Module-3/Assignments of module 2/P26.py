class Engine:
    def engine_type(self):
        print("Engine type: Petrol")

class Car(Engine):
    def wheels(self):
        print("A car has 4 wheels")

class Electric:
    def battery(self):
        print("Battery: Lithium-ion")

class ElectricCar(Car, Electric):
    def model(self):
        print("Tesla Model 3")

tesla = ElectricCar()

tesla.engine_type()  
tesla.wheels()       
tesla.battery()      
tesla.model()        
