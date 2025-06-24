from calculator import  Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width + self.length * 2

    def __str__(self):
        return f"the length of rectangle is {self.length}, the width of rectangle is {self.width}"
    def __repr__(self):
        return  f"rectangle({self.length},{self.width})"
