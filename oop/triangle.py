
from oop.calculator import Shape


class Triangle(Shape):

    def __init__(self,length, width):
        self.side_length = length
        self.side_width = width

    def get_area(self):
        return (self.side_length * self.side_width) / 2

    def get_perimeter(self):
        return (self.side_length **2 + self.side_width **2) ** .5 + self.side_length + self.side_width

    def __str__(self):
        return f"the length of triangle is {self.side_length}, the width of triangle is {self.side_width}"

    def __repr__(self):
        return f"Triangle({self.side_length},{self.side_width})"

    def __add__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError("error!")
        new_side_length = self.side_length + other.side_length
        new_side_width = self.side_width + other.side_width
        return Triangle(new_side_length,new_side_width)