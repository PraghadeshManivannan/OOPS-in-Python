class Rentalsystem:

    def __init__(self):
        self.availableCars = ['SUV','SEDAN','HATCHBACK']
        self.rentForCars = [100,50,30]

    def displayAvailableCars(self):
        print()
        print("Available Cars and their price for 1 day in dollars")
        for i in range(len(self.availableCars)):
            print(f'The price for { self.availableCars[i] } is { self.rentForCars[i] }')    
        

    def lendCar(self,requestedCar):
        
        if requestedCar in self.availableCars:
            days = int(input(f"Enter the number of days requested for { requestedCar }:"))
            index1 = self.availableCars.index(requestedCar)
            fare = self.rentForCars[index1] * days
            print(f"The fare for the car will be { fare } dollars")
            n = int(input("If you want to book press 1:"))
            if n == 1:
                print(f'You have borrowed the Car { requestedCar} successfully')
                del(self.rentForCars[index1])
                self.availableCars.remove(requestedCar)
            else:
                print("Try other cars")

        
        else:
            print("Sorry the Car is not available in the Rental System")
        

    def addCar(self,returnedCar):

        self.availableCars.append(returnedCar)
        if returnedCar == 'SUV':
            self.rentForCars.append(100)
        elif returnedCar == 'SEDAN':
            self.rentForCars.append(50)
        elif returnedCar == 'HATCHBACK':
            self.rentForCars.append(30)
        else:
            self.rentForCars.append(50)
        print(f'You have returned the Car { returnedCar }. Thank You!!')
        

class Customer:
    def requestCar(self):
        self.Car = input("Enter the name of a Car you would like to borrow:")
        return self.Car.upper()

    def returnCar(self):
        self.Car = input("Enter the name of a Car you would like to return:")
        return self.Car.upper()

rentalSystem = Rentalsystem()
customer = Customer()

while(1):
    
    print('1.Available Cars 2.Borrow Car 3.Return Car 4.Exit')
    n = int(input('Enter your choice:'))

    if n == 1:
        rentalSystem.displayAvailableCars()

    elif n == 2:
        rentalSystem.lendCar(customer.requestCar()) 
    
    elif n == 3:
        rentalSystem.addCar(customer.returnCar())
    
    elif n == 4:
        break

