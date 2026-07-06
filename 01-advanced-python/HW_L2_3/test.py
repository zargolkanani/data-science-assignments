from Geometry.square import Square
from Geometry.circle import Circle
from Geometry.rectangle import Rectangle
from Geometry.triangle import Triangle


shape_list = [Square(2), Circle("5"),Square(-1), Rectangle(2, "-1"), Rectangle(2, 8), Triangle(0, -1, 5)]

# write in a file
with open("shape_output.txt", "w") as file:
    for shape in shape_list:
        if shape.valid:
            file.write(f"Shape : {shape.__class__.__name__} - Area : {shape.area()} - Prerimeter : {shape.perimeter():.2f}\n")
        else:
            file.write(f"Shape : {shape.__class__.__name__} - Error : {shape.errors}\n")
            



