from Geometry.shape import Shape

class Rectangle(Shape):
    
    def __init__(self, width, length):
        # initialize parent class (sets defulat values like valid = True , errors=[])        
        super().__init__()

        # validate input type
        if not isinstance(length , (int , float)) or not isinstance(width , (int , float)):
            self.valid = False
            self.errors.append("Invalid data type!")

        # validate values (must be positive number)
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            if length <= 0 or width <= 0:
                self.valid = False
                self.errors.append("Invalid length or width!")
                
        # assign values only if input is valid 
        if self.valid:     
            self.width = width
            self.length = length

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return 2 * (self.width + self.length) 
