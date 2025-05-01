class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        

class ElectricCar(Car):
    def __init__(self, brand, model,color, batterySize):
        super().__init__(model, brand, color)
        self.batterySize = batterySize
        
myElectricCar = ElectricCar("TATA", "Nexon", "red", "1000KWH")

print(isinstance(myElectricCar, Car))
print(isinstance(myElectricCar, ElectricCar))
