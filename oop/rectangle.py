from calculator import  Shape

class Rectangle(Shape):
    def __init__(self, side_length, side_width):
        if side_length <= 0 or side_width <= 0:
            raise ValueError("the length and width must be positive number.")
        self.side_length = side_length
        self.side_width = side_width

    def get_area(self):
        return self.side_width * self.side_length

    def get_perimeter(self):
        return (self.side_width + self.side_length) * 2

    def __str__(self):
        return f"the length of rectangle is {self.side_length}, the width of rectangle is {self.side_width}"
    def __repr__(self):
        return  f"rectangle({self.side_length},{self.side_width})"
