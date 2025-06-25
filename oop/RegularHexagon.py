import  math
from  square import Square

class RegularHexagon(Square):
    def __init__(self,side_length):
        super().__init__(side_length)
    def get_area(self):
        return (math.sqrt(3) * 3 * (self.length ** 2)) / 2
    def get_perimeter(self):
        return self.length * 6
    def __str__(self):
        return f"the side length of regular hexagon is {self.length}"
    def __repr__(self):
        return f"regular hexagon ({self.length})"