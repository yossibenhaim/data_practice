from calculator import  Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width + self.length * 2
