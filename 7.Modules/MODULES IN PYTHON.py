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
# Create randomer_number below:
random_list = [random.randint(1, 100) for i in range(101)]

# Create a new variable randomer_number and set it equal to random.choice() with random_list as an argument.
# Print randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number out to see what number was picked!
print(randomer_number)
