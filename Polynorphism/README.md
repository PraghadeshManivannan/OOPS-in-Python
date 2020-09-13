# Polymorphism
### Polymorphism
The same interface existing in different forms is called polymorphism
#### Example :
    An addition between two integers 2 + 2 return 4 whereas an addition between two strings "Hello" + "World" concatenates it to "Hello World"
### Operator overloading 
Redefining how an operator operates its operands is called operator overloading.
#### Syntax:
    def __operatorFunction__(operandOne, operandTwo):
      # Define the operation that has to be performed

### Overriding
Modifying the inherited behaviour of methods of a base class in a derived class is called overriding.
#### Syntax:
    class BaseClass:
      def methodOne(self):
        # Body of method
    class DerivedClass(baseClass):
      def methodOne(self):
        # Redefine the body of methodOne

### Super() 
super() is used to access the methods of base class.
#### Example:
      class BaseClass:
        def baseClassMethod():
          print("This is BaseClassOne")
      class DerivedClass(BaseClass):
        def __init__(self):
          # calls the base class method
      super().baseClassMethod()
