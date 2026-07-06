# Zargol Kanani

class Vehicle:

    # initialize vehicle informaton
    def __init__(self, brand : str, model : str, year : int, max_speed : int):
        self.brand = brand
        self.__model = model # private attribute
        self.year = year
        self.max_speed = max_speed

    # getter for private attribute : model
    @property
    def model(self):
        return self.__model
    
    # setter for private attribute : model
    @model.setter
    def model(self, value):
        self.__model = value

    def calculate_price(self):
        price =  (self.max_speed * 10) + self.year
        return price
    
    # compare 2 vehicles: 2 objects of vehicle are equal if their brand or max_speed are equal
    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return self.brand == other.brand or self.max_speed == other.max_speed

    # return formatted information    
    def get_information(self):
        return (f"brand: {self.brand}\nmodel: {self.model}\nyear: {self.year}\nmax_speed: {self.max_speed}")

    def __str__(self):
        return self.get_information()

class Car(Vehicle):

    def __init__(self, brand, model, year, max_speed, doors, fuel_type):
        super().__init__(brand, model, year, max_speed)
        self.doors = doors
        self.fuel_type = fuel_type

    # override to include car-specific info
    def get_information(self):
        return (f"{super().get_information()}\ndoors: {self.doors}\nfuel_type: {self.fuel_type}")
    


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, max_speed, engine_capacity : int):
        super().__init__(brand, model, year, max_speed)
        self.engine_capacity = engine_capacity

    # override price calculation for motorcycle
    def calculate_price(self):
        price =  self.engine_capacity + ( 5 * self.max_speed ) + self.year
        return price
    
    def get_information(self):
        return (f"{super().get_information()}\nengine_capacity: {self.engine_capacity}")    

    
class Bicycle(Vehicle):
    def __init__(self, brand, model, year, max_speed, size):
        super().__init__(brand, model, year, max_speed)
        self.size = size

    def get_information(self):
        return (f"{super().get_information()}\nsize: {self.size}")


# ----test-----
car1 = Car('BMW', 'X5', 2020, 240, 4, 'gas')
car2 = Car('Audi', 'A4', 2018, 220, 4, 'diesel')
motor = Motorcycle('Honda','CBR500', 2020, 180, 500)
bicycle = Bicycle('Trek', 'FX2', 2021, 30, 'L')
# print(bicycle)
# print(car1)
# print(motor)
# print(bicycle.model)
# bicycle.model = "Escape 3"
# print(bicycle.model)
# print(motor.calculate_price())
# print(motor)
# print(car1 == car2)

