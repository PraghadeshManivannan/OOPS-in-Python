class Library:

    def __init__(self):
        self.availableBooks = ['Think Like A Monk', 'Attitude is Everything', 'Who will cry when you die']

    def displayAvailableBooks(self):
        print("Available Books")
        print(" ".join(self.availableBooks))

    def lendBook(self,requestedBook):
        
        if requestedBook in self.availableBooks:
            print(f"You have borrowed the book { requestedBook } successfully")
            self.availableBooks.remove(requestedBook)
        
        else:
            print("Sorry the book is not available in the library")
        

    def addBook(self,returnedBook):

        self.availableBooks.append(returnedBook)
        print(f'You have returned the book { returnedBook }. Thank You!!')
        

class Customer:
    def requestBook(self):
        self.book = input("Enter the name of a book you would like to borrow:")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of a book you would like to return:")
        return self.book

library = Library()
customer = Customer()

while(1):
    
    print('1.Available books 2.Borrow Book 3.Return Book 4.Exit')
    n = int(input('Enter your choice:'))

    if n == 1:
        library.displayAvailableBooks()

    elif n == 2:
        library.lendBook(customer.requestBook()) 
    
    elif n == 3:
        library.addBook(customer.returnBook())
    
    elif n == 4:
        break

