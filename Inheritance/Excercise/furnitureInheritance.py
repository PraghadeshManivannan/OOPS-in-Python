class Furniture:
    woodType = 'Teakwood'
    __numberOfLegs = 4


class Chair(Furniture):

    def changeWood(self):
        wood = input('Enter the type of wood you needed:')
        self.woodType = wood


furniture = Furniture()

while(1):
    print('1.Details of chair 2.Change the wood of the chair 3.Exit')
    n = int(input("Enter your choice:"))
    chair = Chair()
    if n == 1:
        print(f'The chair is made with { chair.woodType } and it has {furniture._Furniture__numberOfLegs} legs \n')

    
    elif n == 2:
        chair.changeWood()
        print(f'The chair is made with { chair.woodType } and it has {furniture._Furniture__numberOfLegs} legs \n')


    elif n == 3:
        break

    else:
        print('Enter the correct choice \n')
 
    

