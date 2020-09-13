class Bike:
    wheels = 2
    _color = 'Black'
    __name = 'Himalayan'

class RoyalEnfield(Bike):
    def __init__(self):
        print(f'Protected specifiers color is { self._color }')

bike = Bike()
re =  RoyalEnfield()
print(f'Public Attribute number of wheels = { bike.wheels }')
print(f'Private attribute bike name = {bike._Bike__name}')