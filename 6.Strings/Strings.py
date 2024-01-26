# Lesson 1 Introduction to Strings
# 1.Introduction to Strings
# In Python, the way we store something like a word, a sentence, or even a whole paragraph
# is as a string. A string is a sequence of characters contained within a pair of 'single quotes' or "double quotes".
# A string can be any length and can contain any letters, numbers, symbols, and spaces.

# We will learn how to slice strings, select specific characters from strings, search strings for characters, iterate
# through strings, and use strings in conditional statements.
#
# Let’s get started.


# Save your favorite word as a string to the variable favorite_word.
favorite_word = 'Strong'

# Print favorite_word.
print(favorite_word)

# 2.They're all Lists!
# A string can be thought of as a list of characters. Like any other list, each character in a string has an index.
# We can select specific letters from this string using the index.

# One of the most common things that are represented by strings is names.
# Save your name as a string to the variable my_name.
my_name = 'Steven'

# Select the first letter of the variable my_name and save it to first_initial.
first_initial = my_name[0]

# 3.Cut Me a Slice of String
# Not only can we select a single character from a string, but we can also select entire
# chunks of characters from a string. We can do this with the following syntax:string[first_index:last_index]

# This is called slicing a string. When we slice a string we are creating a substring - a brand new string that starts
# at (and includes) the first_index and ends at (but excludes) the last_index.

# A new employee, Rodrigo Villanueva, is starting today and you need to create his account. His first_name and
# last_name are stored as strings:
first_name = "Rodrigo"
last_name = "Villanueva"
# Create a variable new_account by slicing the first five letters of his last_name.
new_account = last_name[:5]

# Create a variable called temp_password by creating a slice out of the third through sixth letters of last_name.
temp_password = last_name[2:6]

# 4.Concatenating Strings
# We can also concatenate, or combine, two existing strings together into a new string.

# Write a function called account_generator() that takes two inputs, first_name and last_name and concatenates the
# first three letters of each and then returns the new account name.
first_name = "Julie"
last_name = "Blevins"


def account_generator(firstname, lastname):
    new_account_name = firstname[:3] + lastname[:3]
    return new_account_name


# Test your function on the first_name and last_name provided and save it to the variable new_account.
new_account = account_generator(first_name, last_name)

# 5.More and More String Slicing (How Long is that String?)
# Python comes with some built-in functions for working with strings. One of the most commonly used of these functions
# is len(). len() returns the number of characters in a string:


# Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates
# the last three letters of each and returns them as a string.
first_name = "Reiko"
last_name = "Matsuki"


def password_generator(firstname, lastname):
    length1 = len(firstname)
    length2 = len(lastname)
    return firstname[length1 - 3:] + lastname[length2 - 3:]


# Test your function on the provided first_name and last_name and save it to the variable temp_password.
temp_password = password_generator(first_name, last_name)
print(temp_password)

# 6.Negative Indices
# In the previous exercise, we used len() to get a slice of characters at the end of a string.
#
# There’s a much easier way to do this — we can use negative indices! Negative indices count backward from the end of
# the string, so string_name[-1] is the last character of the string, string_name[-2] is the second last character of
# the string, etc.

# Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]

# Use negative indices to create a slice of the last 4 characters in company_motto.
# Save this to the variable final_word.
final_word = company_motto[-4:]

# 7.Strings are Immutable
# So far in this lesson, we’ve been selecting characters from strings, slicing strings,
# and concatenating strings. Each time we perform one of these operations we are creating an entirely new string.

# This is because strings are immutable. This means that we cannot change a string once it is created. We can use it
# to create other strings, but we cannot change the string itself.

# Try changing the first character of first_name by running first_name[0] = "R"
first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"
# TypeError: 'str' object does not support item assignment

# Oh right! Strings are immutable, so we can’t change an individual character.
# Okay that’s no problem—we can still fix this! Delete the code you just wrote for step 1.Then, concatenate the
# string "R" with a slice of first_name that includes everything but the first character, "B",
# and save it to a new string fixed_first_name.
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

# 8.Escape Characters
# We’ll have accidentally ended the string before we wanted to by including the " character. The way we can do this is
# by introducing escape characters. By adding a backslash in front of the special character we want to escape, \",
# we can include it in a string.

# When Rob Daily  set up his account he set his password to be theycallme"crazy"91
# password = "theycallme"crazy"91"

# His password was causing some errors in the system because of the " marks. Rewrite his password using escape
# characters and save it to the variable password.
password = "theycallme\"crazy\"91"
print(password)


# 9.Iterating through Strings
# Because strings are lists, that means we can iterate through a string using for or while loops. This opens up a whole
# range of possibilities of ways we can manipulate and analyze strings.

# Write a new function called get_length() that takes a string as an input and returns the number of characters in that
# string. Do this by iterating through the string. Do not use the len() function!
def get_length(string):
    length = 0
    for letter in string:
        length += 1
    return length


length = get_length("manipulate")
print(length)


# 10.Strings and Conditionals (Part One)
#  When we iterate through a string we do something with each character. By including conditional statements inside of
#  these iterations, we can start to do some really cool stuff.

# Write a function called letter_check that takes two inputs, word and letter.
# This function should return True if the word contains the letter and False if it does not
def letter_check(word, letter):
    for i in word:
        if i == letter:
            return True
    return False


# We tested your function using letter_check("strawberry", "a") and expected it to return True
print(letter_check("strawberry", "a"))

# We tested your function using letter_check("strawberry", "o") and expected it to return False
print(letter_check("strawberry", "o"))

# 11.Strings and Conditionals (Part Two)
# There’s an even easier way than iterating through the entire string to determine if a character is in a string.
# We can do this type of check more efficiently using in. in checks if one string is part of another string.
# Here, letter in word is a boolean expression that is True if the string letter is in the string word.
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

# In fact, this method is more powerful than the function you wrote in the last exercise because it not only works with
# letters, but with entire strings as well.
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False

# It can be helpful to include more than one boolean expression in the same line of code. To do this, use and or and
# not in between the boolean expressions.
print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")


# => True

# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string
# contains little_string.
# or example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False


print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))


# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list
# with all of the letters they have in common.The letters in the returned list should be unique.
# Expected the test common_letters('manhattan', 'san francisco') to return [‘a’, ‘n’]
def common_letters(string_one, string_two):
    common = []
    for i in string_one:
        for j in string_two:
            if i == j and not i in common:
                common.append(i)
    return common


print(common_letters('manhattan', 'san francisco'))


# 12.Review Let’s start with username_generator. Create a function called username_generator take two inputs,
# first_name and last_name and returns a user_name. The username should be a slice of the first three letters of
# their first name and the first four letters of their last name. If their first name is less than three letters or
# their last name is less than four letters it should use their entire names.
#
# For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.
def username_generator(first_name, last_name):
    if len(first_name) < 3 or len(last_name) < 4:
        user_name = first_name + last_name
    else:
        user_name = first_name[:3] + last_name[:4]
    return user_name


print(username_generator("Abe", "Simpson "))


# Great work! Now for the temporary password, they want the function to take the input user name and shift all of the
# letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For
# example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.
#
# Start by defining a function called password_generator that takes one parameter user_name and defines an empty
# string named password within the function body.
def password_generator(user_name):
  password = ""
  password = user_name[-1:] + user_name[0:-1]
  return password

print(password_generator("AbeSimp"))

# Inside password_generator, create a for loop that iterates through the indices of user_name by going from 0 to len(
# user_name).
#
# The loop should create the password by shifting all the letters of user_name one to the right. To do so,
# add the letter at the previous index of user_name to password with each pass of the loop.
#
# After the for loop but still within the definition of password_generator, return the password.
