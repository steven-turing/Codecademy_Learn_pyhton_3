# 1.Types
# We can check the type of a Python variable using the type() function.A variable’s type determines what you can
# do with it and how you can use it.
print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))


# 2.Class
# Define a class using the class keyword.
class Facade:
    pass


# 3.Instantiation
# A class doesn’t accomplish anything simply by being defined. A class must be instantiated. In other words, we must
# create an instance of the class, in order to breathe life into the schematic.
class Facade:
    pass


facade_1 = Facade()


# 4.Object-Oriented Programming
# A class instance is also called an object. The pattern of defining classes and creating objects to represent the
# responsibilities of a program is known as Object Oriented Programming or OOP.
# Instantiation takes a class and turns it into an object, the type() function does the opposite of that.
class Facade:
    pass


facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)


# 5.Class Variables
# When we want the same data to be available to every instance of a class we use a class variable. A class variable is a
# variable that’s the same for every instance of the class.
#
# You can define a class variable by including it in the indented part of your class definition, and you can access all
# of an object’s class variables with object.variable syntax.
class Grade:
    minimum_passing = 65


# 6.Methods
# Methods are functions that are defined as part of a class. The first argument in a method is always the object that is
# calling the method. Convention recommends that we name this first argument self. Methods always have at least this one
# argument.
class Rules:
    def washing_brushes(self):
        return ("Point bristles towards the basin while washing your brushes.")


# 7.Methods with Arguments
# Methods can also take more arguments than just self
class Circle:
    pi = 3.14

    def area(self, radius):
        return (self.pi * radius ** 2)


circle = Circle()

pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(pizza_area, teaching_table_area, round_room_area)


# 8.Constructors
# Methods that are used to prepare an object being instantiated are called constructors. The word
# “constructor” is used to describe similar features in other object-oriented programming languages, but programmers
# who refer to a constructor in Python are usually talking about the __init__() method.
class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: ", diameter)


teaching_table = Circle(36)


# 9.Instance Variables
# We’ve learned so far that a class is a schematic for a data type and an object is an instance
# of a class, but why is there such a strong need to differentiate the two if each object can only have the methods
# and class variables the class has? This is because each instance of a class can hold different kinds of data.

# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all
# instances of a class — they are variables that are specific to the object they are attached to.
class Store:
    pass


alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# 10.Attribute Functions
# Instance variables and class variables are both accessed similarly in Python. This is no
# mistake, they are both considered attributes of an object. If we attempt to access an attribute that is neither a
# class variable nor an instance variable of the object Python will throw an AttributeError.
# What if we aren’t sure if an object has an attribute or not? hasattr() will return True if an object has a given
# attribute and False otherwise. If we want to get the actual value of the attribute, getattr() is a Python function
# that will return the value of a given object and attribute.
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for i in can_we_count_it:
    if hasattr(i, "count"):
        print(str(type(i)) + " has the count attribute!")
    else:
        print(str(type(i)) + " does not have the count attribute :(")


# 11.Self
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
