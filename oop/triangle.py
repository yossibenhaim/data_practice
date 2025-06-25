from rectangle import Rectangle

class Triangle(Rectangle):

    def get_area(self):
        return (self.side_length * self.side_width) / 2

    def get_perimeter(self):
        return (self.side_length **2 + self.side_width **2) ** .5 + self.side_length + self.side_width

    def __str__(self):
        return f"the length of triangle is {self.side_length}, the width of triangle is {self.side_width}"

    def __repr__(self):
        return f"Triangle({self.side_length},{self.side_width})"