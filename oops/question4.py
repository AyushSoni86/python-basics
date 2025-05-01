class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        
myCar = Car("Model S", "Tesla", "red")

print(myCar.get_color())
myCar.set_color("blue")
print(myCar.get_color())
