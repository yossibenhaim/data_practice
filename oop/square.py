from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self,side_length):
        super().__init__(side_length,side_length)

    def __str__(self):
        return f"the width of square is {self.side_length}"

    def __repr__(self):
        return f"Square({self.side_length})"

    def __add__(self,rectangle):
        if not isinstance(rectangle,Rectangle):
            raise TypeError("error!")
        if rectangle.side_width != rectangle.side_length:
            raise TypeError("error!")
        temp = Rectangle(self.side_length + rectangle.side_length,self.side_width + rectangle.side_width)
        return  temp
