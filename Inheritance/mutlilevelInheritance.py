class Intel:
    manufacturer = 'Intel Corporation'
    contactDetail = 'www.intel.org/contact'
    
    def printDetails(self):
        print(f'To contact us, visit { self.contactDetail }')

class OperatingSystem:
    core = 12
    threads = 24
    multitasking = True

class Processor(OperatingSystem,Intel):
    yearOfManufacture = 2020
    name = 'Intel i9 10th gen'
    
    def details(self):
        print(f'The { self.name } processor was manufactured in the year { self.yearOfManufacture } by { self.manufacturer }')
        if self.multitasking is True:
            print(f'It has { self.core } cores and { self.threads } threads')

class Laptop(Processor):
    def __init__(self):
        self.price = 100000
        print(f'The laptop with { self.name} processor with {self.core} cores and {self.threads} threads manufactured by { self.manufacturer } will cost around {self.price}')

i9 = Laptop()

i9.details()

i9.printDetails()
