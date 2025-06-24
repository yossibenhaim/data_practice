from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return f"the with of square is {self.width}"

    def __repr__(self):
        return f"square({self.width})"