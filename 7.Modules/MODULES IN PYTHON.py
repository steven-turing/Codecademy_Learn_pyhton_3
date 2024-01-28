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