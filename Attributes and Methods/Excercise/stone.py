class Preciousstone:
    
    def __init__(self):
        self.preciousStone = []
    
    def storePreciousStone(self,name):
        self.preciousStone.append(name)
        if( len(self.preciousStone) > 5):
            del(self.preciousStone[0])
        
    
    def displayPreciousStone(self):
        if( len(self.preciousStone) > 0):
            print(' '.join(self.preciousStone))

preciousstone = Preciousstone()

while(1):
   
    print('1.Store 2.Display 3.Exit')
    
    n = int(input('Enter your choice:'))
    
    if n == 1:
        stone = input("Enter the stone name:")
        preciousstone.storePreciousStone(stone)
   
    if n == 2:
        preciousstone.displayPreciousStone()
   
    if n == 3:
        break