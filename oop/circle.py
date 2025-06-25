import  math
from  square import Square

class Circle(Square):

    def __init__(self,radius):
        super().__init__(radius)

    def get_area(self):
        return  math.pi * (self.length ** 2)

    def get_perimeter(self):
        return  self.length * math.pi * 2

    def __str__(self):
        return  f"the radius of circle is {self.length}"
    def __repr__(self):
        return  f"circle({self.length}"

