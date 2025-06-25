import  math
from  calculator import Shape

class Circle(Shape):

    def __init__(self,radius):
        if radius <= 0:
            raise ValueError("the radius must be positive number.")
        self.radius = radius

    def get_area(self):
        return  math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return  (self.radius * math.pi) * 2

    def __str__(self):
        return  f"the radius of circle is {self.radius}"
    def __repr__(self):
        return  f"Circle({self.radius})"

