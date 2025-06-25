import  math
from  square import Square

class RegularHexagon(Square):

    def get_area(self):
        return (math.sqrt(3) * 3 * (self.side_length ** 2)) / 2

    def get_perimeter(self):
        return self.side_length * 6

    def __str__(self):
        return f"the side length of regular hexagon is {self.side_length}"

    def __repr__(self):
        return f"regular hexagon ({self.side_length})"