from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self,side_length):
        super().__init__(side_length,side_length)


    def __str__(self):
        return f"the width of square is {self.side_length}"

    def __repr__(self):
        return f"square({self.side_length})"