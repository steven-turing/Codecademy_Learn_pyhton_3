# 1.Welcome
# Python is a programming language. Like other languages, it gives us a way to communicate ideas.
# In the case of a programming language, these ideas are “commands” that people use to communicate with a computer!
# Change Codecademy to your name in the script to the right. Run the code to see what it does!
# As soon as you’re ready, move on to the next exercise to begin learning to write your own Python programs!

my_name = "Codecademy"
print("Hello and welcome " + my_name + "!")

my_name = "SiJinWen"
print("Hello and Welcome " + my_name + "!")

# 2.Comments
# Ironically, the first thing we’re going to do is show how to tell a computer to ignore a part of a program.
# Text written in a program but not run by the computer is called a comment.
# Python interprets anything after a # as a comment.

# my first program :  spider chinamoney website

# 3.Print Now what we’re going to do is teach our computer to communicate. The gift of speech is valuable: a computer
# can answer many questions we have about “how” or “why” or “what” it is doing. In Python, the print() function is
# used to tell a computer to talk. The message to be printed should be surrounded by quotes:

print("Hello world!")

# 4.Strings
# Computer programmers refer to blocks of text as strings. In our last exercise, we created the string “Hello world!”.
# In Python a string is either surrounded by double quotes ("Hello world") or single quotes ('Hello world').
# It doesn’t matter which kind you use, just be consistent.

print('My name is "Steven".')

# 5.Variables
# Programming languages offer a method of storing data for reuse.
# If there is a greeting we want to present, a date we need to reuse,
# or a user ID we need to remember we can create a variable which can store a value.
# In Python, we assign variables by using the equals sign (=).

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = 'noodles'

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = 'BBQ'
# Printing out dinner
print("Dinner:")
print(meal)

# 6.Errors
# Python refers to these mistakes as errors and will point to the location where an error occurred with a ^ character.
# Two common errors that we encounter while writing Python are SyntaxError and NameError.
# You might encounter a SyntaxError if you open a string with a single quote and end it with double quotes.
# Update the string so that it starts and ends with the same punctuation.
# print("This message has mismatched quote marks!')
# You might encounter a NameError if you try to print a single word string but fail to put any quotes around it.
# print(Abracadabra)

# 7.Numbers
# Computers can understand much more than just strings of text.
# An integer, or int, is a whole number.
# Define the release and runtime integer variables below:
release_year = 1988
runtime = 10000

# A floating-point number, or a float, is a decimal number.
# Define the rating_out_of_10 float variable below:

rating_out_of_10 = 8.8

# 8.Calculations
# Computers absolutely excel at performing calculations.
# Python performs the arithmetic operations of addition, subtraction, multiplication, and division with +, -, *, and /.

print(25 * 68 + 13 / 28)

# 9.Changing Numbers
# Variables that are assigned numeric values can be treated the same as the numbers themselves.
# Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing
# between the variables and literals (like the number 2 in this example).
# Performing arithmetic on variables does not change the variable — you can only update a variable using the = sign.
quilt_width = 8
quilt_length = 12
squares = quilt_width * quilt_length
print(squares)

quilt_length = 8
squares = quilt_width * quilt_length
print(squares)

# 10.Exponents
# Python can also perform exponentiation. In written math, you might see an exponent as a superscript number,
# but typing superscript numbers isn’t always easy on modern keyboards.
# Since this operation is so related to multiplication, we use the notation **.
# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?

print(6 * 6 * 6 * 6)

# 11.Modulo
# Python offers a companion to the division operator called the modulo operator.
# The modulo operator is indicated by % and gives the remainder of a division calculation.
# If the two numbers are divisible, then the result of the modulo operation will be 0.

order_263_r = 263 % 11
print(order_263_r)

order_263_coupon = "no"

order_264_r = 264 % 11
print(order_264_r)

order_264_coupon = "yes"

# 12.Concatenation
# The + operator doesn’t just add two numbers, it can also “add” two strings!
# The process of combining two strings is called string concatenation.
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6
# print(message)
print(message)

# 13.Plus Equals
# Python offers a shorthand for updating variables.
# When you have a number saved in a variable and want to add to the current value of the variable,
# you can use the += (plus-equals) operator.
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater
total_price += fun_books
print("The total price is", total_price)

# 14.Multi-line Strings
# Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one,
# we tell the program that the string doesn’t end until the next triple-quote.
# Assign the string here
to_you = '''
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
'''

print(to_you)

# 15.Review
# In this lesson, we accomplished a lot of things! We instructed our computers to print messages, we stored these
# messages as variables, and we learned to update those messages depending on the part of the program we were in.
# We performed mathematical calculations and explored some of the mathematical expressions that Python offers us.
# We learned about errors and other valuable skills that will continue to serve us as we develop our programming skills.

# Good job!

# Here are a few more resources to add to your toolkit:

# Codecademy Docs: Python
# Codecademy Workspaces: Python
# Make sure to bookmark these links so you have them at your disposal.

# This lesson included a video walkthrough. Please answer two quick questions to let us know what you thought of it.
# Your feedback helps us learn and improve.
my_age = 31
print(my_age)

half_my_age = my_age / 2
print(half_my_age)

greeting = "hi , there"
print(greeting)

name = 'sijinwen'

greeting_with_name = greeting + " " + name

print(greeting_with_name)
