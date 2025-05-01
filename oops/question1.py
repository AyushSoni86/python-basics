class Car:
    def __init__(self):
        self.brand = "TATA"
        self.model = "NEXON"
        print("Non parameterized")
       
    def __init__(self, brand, model):  
        self.brand = brand
        self.model = model
        print("Parameterized")
        
myCar = Car("Tata", "Nexon")

print(myCar.brand, myCar.model)