from abc import abstractmethod

class Shape:

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Error:")
        return self.get_area() == other.get_area()