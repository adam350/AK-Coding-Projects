class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
     
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self, radius):
        return 3.14*(radius)**2 
    
    def calculate_perimeter(self, radius):
        return  2*3.14*radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self, length, width):
        return length*width
    
    def calculate_perimeter(self, length, width):
        return 2*(length+width)
    
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self, base, height):
        return 0.5*base*height
    
    def calculate_perimeter(self, side1, side2, side3):
        return side1 + side2 + side3
    
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(5, 3, 7)
]

for shape in shapes:
    print(f"Shape: {type(shape).__name__}")
    print(f"Area: {shape.calculate_area()}")
    print(f"Perimeter: {shape.calculate_perimeter()}")
    print()