class Car:
    def __init__(self, brand=None, model=None):
        self.model = model
        self.brand = brand
        
    def inner(self):
        self.car_description()
        
    @staticmethod
    def car_description():
        print("This is a normal car descrpition")
    
    
myCar = Car()
Car.car_description()
myCar.inner()