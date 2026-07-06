from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        self.valid = True
        self.errors = [] # list to store all validation errors

    # مساحت
    @abstractmethod
    def area(self):
        pass

    # محيط    
    @abstractmethod
    def perimeter(self):
        pass