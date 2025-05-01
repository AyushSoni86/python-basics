class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        
    def displayName(self):
        return self.brand + " and " + self.model
    
    
myCar = Car("Fortuner", "Toyota")
print(myCar.displayName())
