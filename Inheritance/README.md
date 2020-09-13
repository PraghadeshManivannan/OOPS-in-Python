# Inheritance
### Inheritance
Inheriting the attributes and methods of a base class into a derived class is called Inheritance.
#### Syntax:
      class BaseClass:
        # Body of BaseClass
      class DerivedClass(BaseClass):
        # Body of DerivedClass
### Multiple Inheritance
Mechanism in which a derived class inherits from two or more base classes is called a multiple inheritance
#### Syntax:
      class baseClassOne:
        # Body of baseClassOne
      class baseClassTwo:
        # Body of baseClassTwo
      class derivedClass(baseClassOne, baseClassTwo):
        # Body of derived class
### Multilevel Inheritance
Mechanism in which a derived class inherits from a base class which has been derived from another base class is called a multilevel inheritance
#### Syntax:
      class BaseClass:
        # Body of baseClass
      class DerivedClassOne(BaseClass):
        # Body of DerivedClassOne
      class DerivedClassTwo(DerivedClassOne):
        # Body of DerivedClassTwo
### Abstract base class 
A base class which contains abstract methods that are to be overridden in its derived class is called an abstract base class. They belong to the abc module.
#### Example:
      from abc import ABCMeta, abstractmethod
      class Shape(metaclass = ABCMeta):
        @abstractmethod
        def area(self):
          return 0
      class Square(Shape):
        def area(self, side)
          return side * side
### The naming conventions used for private, protected and public members
    Private -> __memberName
    Protected -> _memberName
    Public -> memberName
### Name mangling done for private members
 Name mangling is done by prepending the member name with an underscore and class name.
#### Syntax
    _className__memberName
