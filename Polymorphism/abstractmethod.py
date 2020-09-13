from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):

    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side  =  5
    def area(self):
        return (self.side ** 2)

class Rectangle(Shape):
    length  =  5
    width = 4
    def area(self):
        return (self.length * self.width)

square = Square()
rectangle = Rectangle()
print(f'The area of the square is { square.area() } and the area of rectangle is { rectangle.area() }')