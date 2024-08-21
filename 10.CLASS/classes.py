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

# 6.