from rectangle import Rectangle

class Triangle(Rectangle):

    def get_area(self):
        return (self.length * self.width) / 2

    def get_perimeter(self):
        return (self.width **2 + self.length **2) ** -2

    def __str__(self):
        return f"the length of triangle is {self.length}, the width of triangle is {self.width}"

    def __repr__(self):
        return f"triangle ({self.width},{self.length})"