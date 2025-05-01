class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
        
myElectricCar = ElectricCar("TATA", "Nexon", "1000KWH")
# print("brand = ", myElectricCar.brand, ", model = ", myElectricCar.model, ", battery size = ", myElectricCar.batterySize)


class Father:
    def __init__(self):
        pass
    
    def dance(self):
        print("Dance like Michael Jackson")
        
class Mother:
    def __init__(self):
        pass
    
    def dance(self):
        print("Dance like Marry James")
        
class Child(Father, Mother):
    def __init__(self):
        pass
    
    # def dance(self):
    #     print("Dance like Michael Jackson")
    
child = Child()
child.dance()