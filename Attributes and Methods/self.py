class Employee:

    def employeeDetails(self):
        self.name = 'Jarvis'
        self.age = 21
    
    def displayEmployeeDetails(self):
        print(f"The name of the employee is {self.name} and the age of the employee is {self.age}")

employee = Employee()
employee.employeeDetails()
employee.displayEmployeeDetails()
