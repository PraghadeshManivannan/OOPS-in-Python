class Employee:
    def setWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayWorkingHours(self):
        return self.numberOfWorkingHours

class Trainee(Employee):

    def setWorkingHours(self):
        self.numberOfWorkingHours  = 45

    def resetWorkingHours(self):
        super().setWorkingHours()


employee = Employee()
trainee = Trainee()

employee.setWorkingHours()
print(f'The number of working hours for employee is { employee.displayWorkingHours() }')

trainee.setWorkingHours()
print(f'The number of working hours for trainee is { trainee.displayWorkingHours() }')

trainee.resetWorkingHours()
print(f'The number of working hours for trainee after reset is { trainee.displayWorkingHours() }')

