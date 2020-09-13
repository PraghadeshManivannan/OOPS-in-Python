class Employee:
    name = 'Jarvis'
    designation = 'Sales Executive'
    salesMadeThisWeek = 6
    def achievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target have been achieved")
        else:
            print("Target have not been achieved")
    def changeName(self):
        n = input("Enter the name to be changed:")
        self.name = n

employeeOne = Employee()

#print( employeeOne.name + ' ' + employeeOne.designation + ' ' + str(employeeOne.salesMadeThisWeek))
# employeeOne.achievedTarget()

print(f"The name before changing is {employeeOne.name} ")

employeeOne.changeName()

#print( employeeOne.name + ' ' + employeeOne.designation + ' ' + str(employeeOne.salesMadeThisWeek))

print(f"The name after changing is {employeeOne.name} ")