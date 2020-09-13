class Square:
    def __init__(self,side):
        self.side = side

    def __pow__(squareOne,squareTwo):
        return(squareOne.side ** squareTwo.side)


squareOne = Square(2)
squareTwo = Square(8)

print(f'The exponential of { squareOne.side } to the the power { squareTwo.side } is { squareOne ** squareTwo }')