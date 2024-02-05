# Lesson 1 MODULES IN PYTHON
# 1.Modules Python Introduction
# In the world of programming, we care a lot about making code reusable. In most cases, we write code so that it can be
# reusable for ourselves. But sometimes we share code that’s helpful across a broad range of situations.

# In this lesson, we’ll explore how to use tools other people have built in Python that are not included automatically
# for you when you install Python. Python allows us to package code into files or sets of files called modules.

# Usually, to use a module in a file, the basic syntax you need at the top of that file is:
# from module_name import object_name

# One common library that comes as part of the Python Standard Library is datetime. datetime helps you work with dates
# and times in Python.Let’s get started by importing and using the datetime module.

# Import datetime from datetime below:
from datetime import datetime

# Create a variable current_time and set it equal to datetime.now().
current_time = datetime.now()

# Print out current_time.
print(current_time)

# 2.Modules Python Random
# Another one of the most commonly used is random which allows you to generate numbers or select items at random.
# With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:
# import random

# We’ll work with two common random functions:
#
# random.choice() which takes a list as an argument and returns a number from the list
# random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed
# in

# import the random library
import random

# Create a variable random_list and set it equal to an empty list
random_list = []

# Turn the empty list into a list comprehension that uses random.randint() to generate a random integer between 1 and
# 100 (inclusive) for each number in range(101).
random_list = [random.randint(1, 100) for i in range(101)]

# Create a new variable randomer_number and set it equal to random.choice() with random_list as an argument.
# Print randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number out to see what number was picked!
print(randomer_number)

# 3.Modules Python Namespaces
# Notice that when we want to invoke the randint() function we call random.randint().
# This is default behavior where Python offers a namespace for the module. A namespace isolates the functions,
# classes, and variables defined in the module from the code in the file doing the importing. Your local namespace,
# meanwhile, is where your code is run.

# import pyplot from the module matplotlib with the alias plt.(pycharm:File->Settings->project->python interpreter
# -> + -> matplotlib->Install Package)
# Import random below the other import statements. It’s best to keep all imports at the top of your file.
from matplotlib import pyplot as plt
import random

# Create a variable numbers_a and set it equal to the range of numbers 1 through 12 (inclusive).
numbers_a = range(1, 13)

# Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000).
# Feel free to print numbers_b to see your random sample of numbers.
numbers_b = random.sample(range(1000), 12)
print(numbers_b)

# Now let’s plot these number sets against each other using plt. Call plt.plot() with your two variables as its
# arguments.
plt.plot(numbers_a, numbers_b)

# Now call plt.show() and run your code! You should see a graph of random numbers displayed. You’ve used two Python
# modules to accomplish this (random and matplotlib).
plt.show()

# 4.Modules Python Decimals
# Let’s say you are writing software that handles monetary transactions. If you used Python’s built-in floating-point
# arithmetic to calculate a sum, it would result in a weirdly formatted number.
cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)
# =>0.44999999999999996

# Being familiar with rounding errors in floating-point arithmetic you want to use a data type that performs decimal
# arithmetic more accurately. You could do the following:
from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)
# => 0.45

# Use Decimal to make two_decimal_points only have two decimals points and four_decimal_points to only have four
# decimal points.
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)


# 5.Modules Python Files and Scope
# You may remember the concept of scope from when you were learning about functions in Python. If a variable is defined
# inside of a function, it will not be accessible outside of the function.

# Scope also applies to classes and to the files you are working within.
# Tab over to library.py and define a function always_three() with no parameters that returns 3.
# Add your always_three() function below:
# create library.py
def always_three():
    return 3

# Call your always_three() function in script.py. Check out that error message you get in the output terminal and the
# consequences of file scope.
# Resolve the error with an import statement at the top of script.py that imports your function from library. Run your
# code and watch import do its magic!
# Import library below:
# create script.py
#from library import always_three

# Call your function below:
always_three()

# 6.Modules Python Review
# In this lesson, we covered some of the Python Standard Library, but you can explore all the modules that come packaged
# with every installation of Python at the Python Standard Library documentation.
#
# This is just the beginning. Using a package manager (like conda or pip3), you can install any modules available on the
# Python Package Index.
#
# The sky’s the limit!
