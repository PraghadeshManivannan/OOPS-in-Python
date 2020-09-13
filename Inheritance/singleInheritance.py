class Intel:
    manufacturer = 'Intel Corporation'
    contactDetail = 'www.intel.org/contact'
    
    def printDetails(self):
        print(f'To contact us, visit { self.contactDetail }')


class Processor(Intel):
    def __init__(self):
        self.yearOfManufacture = 2020
        self.name = 'Intel i9 10th gen'
    
    def details(self):
        print(f'The { self.name } processor was manufactured in the year { self.yearOfManufacture } by { self.manufacturer }')


i9 = Processor()

i9.details()

i9.printDetails()
