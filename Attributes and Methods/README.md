# Attributes and Methods
### Data Members
Data members are attributes declared within a class.They are properties that further define a class.
There are two types of attributes: class attributes and instance attributes.

#### Class attribute
An attribute that is common across all instances of a class is called a class attribute. Class attributes are accessed by using class name as the prefix.
##### Syntax
    class className:
    classAttribute = value
    
#### Instance attribute
An attribute that is specific to each instance of a class is called an instance attribute. Instance attributes are accessed within an instance method by making use of the self object.
##### Syntax:
    class className:
      def methodName(self):
        self.instanceAttribute = value
     
#### Self Parameter
Every instance method accepts has a default parameter that is being accepted. By convention, this parameter is named self. The self parameter is used to refer to the attributes of that
instance of the class
##### Example:
    class Employee:
      def setName(self, name):
        self.name = name
      
    employee = Employee()
    employee.setName('John')
 

### Methods
A function within a class that performs a specific action is called a method belonging to that class. Methods are of two types: static method and instance method

#### Instance Method
A method which can access the instance attributes of a class by making use of self object is called an instance method

##### Syntax:
      def methodName(self):
        # method body
        
#### Static Method 
A method that does not have access to any of the instance attributes of a class is called a static method. Static method uses a decorator @staticmethod to indicate this method will not be taking the default self parameter.

##### Syntax:
      @staticmethod
      # Observe that self is not being declared since this is a static method
      def methodName():
        # method body
        
#### Init Method
An init method is the constructor of a class that can be used to initialize data members of that class.
It is the first method that is being called on creation of an object.
##### Syntax:
      def __init__(self):
        # Initialize the data members of the class
        
        
### The ways to access the attributes and methods of a class 
      Attributes and methods of a class can be accessed by creating an object and accessing the attributes and objects using class name or object name depending upon the type of
      attribute followed by the dot operator (.) and the attribute name or method name.
