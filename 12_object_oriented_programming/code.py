# ----- Syntax -----
class Animal:
    def __init__(self, name, age, last_name, favourite_colour):
        # Public Attributes
        self.name = name
        self.age = age
        self.distance_moved = 0
        # Protected Attributes
        self._last_name = last_name
        # Private Attributes
        self.__favourite_colour = favourite_colour

    def move(self):
        self.distance_moved += 5

    def favourite_colour(self):
        return self.__favourite_colour

dog = Animal("Johnny", 2, "The Dog", "Green")
print(dog.age)
print(dog.favourite_colour())

# ----- Inheritance -----
class Cat(Animal):
    def __init__(self, name, age, last_name, favourite_colour):
        super().__init__(name, age, last_name, favourite_colour)
        self.sound = "Meow"

    def __str__(self):
        return f"This is {self.name} {self._last_name}, it makes a {self.sound} sound."

class Octopus(Animal):
    def __init__(self, name, age, last_name, favourite_colour):
        super().__init__(name, age, last_name, favourite_colour)
        self.sound = "Blub?"

    def __repr__(self):
        return f"This is {self.name} {self._last_name}, it makes a {self.sound} sound."
        # !r calls this method of the thing

octopus = Octopus("Marie", 700, "The Octopus", "Purple")
cat = Cat("Stitch", 3, "The Cat", "Blue")
print(cat.sound)

# ----- __str__ -----
print(dog) # Ugly Printing
print(cat) # Pretty Printing

# ----- __repr__ -----
# Purpose is to be unambiguous, and if possible what it outputs should allow us to re-create an identical object
print(octopus) # Object

# ----- Types of Methods -----
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method. We don't get any object or class info here.")


instance = ClassTest()
instance.instance_method()
ClassTest.class_method()
ClassTest.static_method()

# You can initialise using a class method
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    # Initialising occurs here instead
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


heavy = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(heavy)
print(light)





