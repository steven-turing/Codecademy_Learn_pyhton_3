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

#6.Relational Operators II
#Now that we’ve added conditional statements to our toolkit for building control flow
#> greater than
#>= greater than or equal to
#< less than
#<= less than or equal to

x = 20
y = 20

# Write the first if statement here:
if x==y:
  print("These numbers are the same")

credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")

#7.Boolean Operators: and
#Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. 
#In these cases, you can build larger boolean expressions using boolean operators.
#There are three boolean operators that we will cover:and or not
#and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.
credits = 120
gpa = 3.4

if credits >= 120 and gpa>=2.0:
  print("You meet the requirements to graduate!")

#8.Boolean Operators: or
#The boolean operator or combines two expressions into a larger expression that is True if either component is True.
credits = 118
gpa = 2.0

if credits >=120 or gpa >=2.0:
  print("You have met at least one of the requirements.")

#9.Boolean Operators: not
#The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. 
#So if we have a True statement and apply a not operator we get a False statement.
credits = 120
gpa = 1.8

if not(credits >= 120):
  print("You do not have enough credits to graduate.")
if not (gpa >=2.0):
   print("Your GPA is not  high enough  to graduate.")
if not (credits >=120) and not (gpa >=2.0):
  print("You do not meet either requirement to graduate!")

#10.Else Statements
#else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

#11.Else If Statements
#An elif statement checks another condition after the previous if statements conditions aren’t met.
grade = 86

if grade >= 90 :
  print("A")
elif grade >= 80 :
   print("B")
elif grade >= 70 :
   print("C")
elif grade >= 60 :
   print("D")
else:
   print("F")

#12.Review
#Great job! We covered a ton of material in this lesson and we’ve increased the number of tools in our Python toolkit by several-fold. 
#Let’s review what we’ve learned this lesson:

#Boolean expressions are statements that can be either True or False
#A boolean variable is a variable that is set to either True or False.
#We can create boolean expressions using relational operators:
#==: Equals
#!=: Not equals
#>: Greater than
#>=: Greater than or equal to
#<: Less than
#<=: Less than or equal to
#if statements can be used to create control flow in your code.
#else statements can be used to execute code when the conditions of an if statement are not met.
#elif statements can be used to build additional checks into your if statements
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)


