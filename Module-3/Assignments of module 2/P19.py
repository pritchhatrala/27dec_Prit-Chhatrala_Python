class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year    

car1 = Car("Toyota", "Fortuner", 2025)

print(f"Brand: {car1.brand}")
print(f"Model: {car1.model}")
print(f"Year: {car1.year}")
