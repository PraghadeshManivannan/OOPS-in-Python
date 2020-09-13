class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def __mul__(rectangleOne,rectangleTwo):
        return(4*(rectangleOne.length + rectangleTwo.length + rectangleTwo.breadth + rectangleOne.breadth))

rectangleOne = Rectangle(10,20)
rectangleTwo = Rectangle(10,5)


print('The sum of two rectangle is',rectangleOne * rectangleTwo)