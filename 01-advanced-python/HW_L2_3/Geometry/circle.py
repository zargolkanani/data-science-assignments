from Geometry.shape import Shape
from math import pi,pow

class Circle(Shape):

    def __init__(self, radius):
        # initialize parent class (sets defulat values like valid = True , errors=[])
        super().__init__()

        # validate input type
        if not isinstance(radius, (int,float)):
            self.valid = False
            self.errors.append("Invalid data type!") 

        # validate values (must be positive number)
        if  isinstance(radius, (int,float)) and radius <= 0 :
            # raise ValueError("Invalid radius!") - my first way
            self.valid = False
            self.errors.append("Invalid radius!")

        # assign values only if input is valid    
        if self.valid: 
            self.radius = radius

    def area(self):
        return  pi * pow(self.radius,2)

    def perimeter(self):
        return 2 * pi * self.radius   

        
