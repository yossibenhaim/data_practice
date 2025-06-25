import  math

from calculator import Shape

class RegularHexagon(Shape):

    def __init__(self,length):
        self.side_length = length

    def get_area(self):
        return (math.sqrt(3) * 3 * (self.side_length ** 2)) / 2

    def get_perimeter(self):
        return self.side_length * 6

    def __str__(self):
        return f"the side length of regular hexagon is {self.side_length}"

    def __repr__(self):
        return f"RegularHexagon({self.side_length})"
    def __add__(self, other):
        if not isinstance(other, RegularHexagon):
            raise TypeError("error!")
        new_side_length = self.side_length + other.side_length
        return RegularHexagon(new_side_length)