#1.Introduction to Control Flow
#This is the control flow of your program. In Python, your script will execute from the top down, until there is nothing
# left to run. It is your job to include gateways, known as conditional statements, to tell the computer when it should
# execute certain blocks of code. If these conditions are met, then run this function.

#2.Boolean Expressions
#In order to build control flow into our program, we want to be able to check if something is true or not.
# A boolean expression is a statement that can either be True or False.

#Example statement:My dog is the cutest dog in the world.
example_statement = "No"
#This is an opinion and not a boolean expression, so you would set example_statement to "No" in the editor to the right.
# Okay, now it’s your turn:
#Statement one:Dogs are mammals.
statement_one = "Yes"
#Statement two:My dog is named Pavel.
statement_two = "Yes"
#Statement three:Dogs make the best pets.
statement_three ="No"
#Statement four:Cats are female dogs.
statement_four ="Yes"

#3.Relational Operators: Equals and Not Equals
#Statement one:(5 * 2) - 1 == 8 + 1
statement_one = True
#Statement two:13 - 6 != (3 * 2) + 1
statement_two = False
#Statement three:3 * (2 - 1) == 4 - 1
statement_three = True

#4.Boolean Variables
#True and False are the only bool types, and any variable that is assigned one of these values is called a boolean
# variable.
my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))

#5.If Statement
#You’ll notice that instead of “then” we have a colon, :. That tells the computer that what’s coming next is what should
#be executed if the condition is met.
# Enter a user name here, make sure to make it a string
user_name = "Dave"

if user_name == "Dave":
  print("Get off my computer Dave!")

user_name = "angela_catlady_87"

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

#6.

