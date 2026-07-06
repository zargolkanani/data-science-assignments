from Geometry.shape import Shape

class Square(Shape):

    def __init__(self, side):
        # initialize parent class (sets defulat values like valid = True , errors=[])        
        super().__init__()

        # validate input type
        if not isinstance(side, (int,float)):
            self.valid = False
            self.errors.append("Invalid data type!")

        # validate values (must be positive number)
        if  isinstance(side, (int,float)) and side <= 0:
            self.valid = False
            self.errors.append("Invalid side!")

        
        # assign values only if input is valid 
        if self.valid:    
            self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4
