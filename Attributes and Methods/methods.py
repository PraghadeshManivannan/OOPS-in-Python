class Employee:

    #init method helps us to overcome the error by calling itself when object is created.No need for calling it once again

    def __init__(self):
        self.name = 'Jarvis'
        self.age = 21

    @staticmethod 
    
    #Statci method helps to overcome the type error when there is no attribute is passed through the method
    
    def welcome():
        print("Welcome to the organization")

    def displayEmployeeDetails(self):
        print(f"The name of the employee is {self.name} and the age of the employee is {self.age}")

employee = Employee()
employee.welcome()
employee.displayEmployeeDetails()
