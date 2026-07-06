from Geometry.shape import Shape
from math import sqrt

class Triangle(Shape):

    def __init__(self, side1, side2  ,side3 ):
        # initialize parent class (sets defulat values like valid = True , errors=[])        
        super().__init__()

        # validate input type
        if not isinstance(side1 , (int , float)) or not isinstance(side2 , (int , float)) or not isinstance(side3 , (int , float)):
            self.valid = False
            self.errors.append("Invalid data type!")

        
        if  isinstance(side1 , (int , float)) and isinstance(side2 , (int , float)) and isinstance(side3 , (int , float)):
            # validate values (must be positive number)
            if side1 <= 0 or side2 <= 0 or side3 <= 0:
                self.valid = False
                self.errors.append("Invalid side") 

            # validate triangle inequality rule:
            # the sum of any two sides must be greater than the third side
            if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
                self.valid = False
                self.errors.append("Invalid triangle!")    
                
        
            
        # assign values only if input is valid 
        if self.valid: 
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3

    
    def area(self):
        # calculate triangle area using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt( s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3  
