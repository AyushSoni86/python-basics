class Car:
    car_count = 0
    def __init__(self, model=None, brand=None):
        self.brand = brand
        self.model = model
        Car.car_count += 1
        
        
carOne = Car()
print(Car.car_count)
carTwo = Car()
print(carTwo.car_count)
carThree = Car()
print(Car.car_count)
        