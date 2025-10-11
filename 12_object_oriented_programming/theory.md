# Object Oriented Programming
## Abstraction
Representation of complex real-world entities as simplified models within your code
- Process of simplifying complex systems by breaking them into smaller, more manageable parts
- Allows you to hide the unnecessary details of an object and expose only the essential features
- Grouping and organisation of variables and functions that fall within the same overarching topic
- EXAMPLE: Class Animal and Sub Classes Cat and Dog represent Abstraction as we only need Animal as a Common Interface

## Encapsulation
Bundling of data and the methods that operate on that data within a single unit called a class
- The concept of bundling data (attributes) and methods (functions) that operate on that data into a single unit class
- EXAMPLE: We use the Class-Specific Variables (Properties) instead of messy Global Variables

## Inheritance
Defining a new class ( derived class or subclass ) based on an existing class ( base class or superclass )
- A mechanism in which a new class (or derived class) is created by inheriting properties and behaviors from an existing class (base or parent)
- Python supports single inheritances, a class can only inherit from one base class

## Polymorphism
 Allows objects of different classes to be treated as objects of a common base class through Method overriding and Method overloading
- Allows objects of different classes to be treated as objects of a common base class
- Enables you to write code that can work with objects of different types in a generic way, as long as they share a common interface
- EXAMPLE: All Animals Eat, so Cat and Dog share eat() as a common function

## Composition
Instead of inheritance, a class can contain multiple classes to simulate real-life scenarios
 
# Classes
## Attributes
**Public**
- Accessible and modifiable anywhere

**Protected**
- Considered non-public and should be accessed using methods
- You can access them outside the class but its best to avoid that

**Private**
- Restricted and have name mangling to make it harder to access them directly from outside the class. can be accessed via methods, otherwise it will produce an attribute error
- This also means Sub Classes can have variables of the same name, but they'll be independent of each other

## Method Annotations
**Instance Methods**
- When you want to produce an action that uses the data stored in an object

**Static Methods**
- Used to just place a method inside a class because you feel it belongs there
- Organisational purposes

**Class Methods**
- Used as factories