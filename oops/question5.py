class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def fuel_type(self):
        print("This is nomal petrol engine")
    
class ElectricCar(Car):
    def __init__(self, brand, model, color, fuelType):
        super().__init__(brand, model, color)
        self.fuelType = fuelType
        
    def fuel_type(self):
        print("This is nomal electric engine")
        
        
myElectricCar = ElectricCar("Suzuki", "Swift Desire", "White", "Electric")

myElectricCar.fuel_type()