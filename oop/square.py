from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self,side_length):
        super().__init__(side_length,side_length)

    def __str__(self):
        return f"the width of square is {self.side_length}"

    def __repr__(self):
        return f"Square({self.side_length})"

    def __add__(self,other):
        if not isinstance(other,Rectangle):
            raise TypeError("error!")
        if other.side_width != other.side_length:
            raise TypeError("error!")
        new_length = self.side_length + other.side_length
        return  Square(new_length)
