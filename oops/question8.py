class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.__brand = brand
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
     
    @property   
    def brand(self):
        return self.__brand
    
myCar = Car("Model S", "Tesla", "red")

print(myCar.brand)
# myCar.brand = "TATA"
# print(myCar.model)
