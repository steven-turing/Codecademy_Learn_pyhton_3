# 1.Introduction
# Python comes with built-in string methods that give you the power to perform complicated tasks on
# strings very quickly and efficiently. These string methods allow you to change the case of a string, split a string
# into many smaller strings, join many small strings together into a larger string, and allow you to neatly combine
# changing variables with string outputs.

# String methods all have the same syntax:string_name.string_method(arguments)

# 2.Formatting Methods
# There are three string methods that can change the casing of a string. These are .lower(), .upper(), and .title().
#   .lower() returns the string with all lowercase characters.
#   .upper() returns the string with all uppercase characters.
#   .title() returns the string in title case, which means the first letter of each word is capitalized.

poem_title = "spring storm"
poem_author = "William Carlos Williams"

# Make poem_title have title case and save it to poem_title_fixed.
poem_title_fixed = poem_title.title()

# Print poem_title and poem_title_fixed.How did the string change?
print(poem_title)
print(poem_title_fixed)

# Make poem_author uppercase and save it to poem_author_fixed.
poem_author_fixed = poem_author.upper()

# Print poem_author and poem_author_fixed. Again, how did the string change?
print(poem_author)
print(poem_author_fixed)

# 3.Splitting Strings
# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given
# argument (which in the case of .split() is known as the delimiter). The following syntax should
# be used:string_name.split(delimiter)

# If you do not provide an argument for .split() it will default to splitting at spaces.
# .split() returned a list with each word in the string.
man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())

# Use .split() to create a list called line_one_words that contains each word in this line of poetry.
line_one = "The sky has given over"
line_one_words = line_one.split()

# 4.Splitting Strings II
# If we provide an argument for .split() we can dictate the character we want our string to be split on. This argument
# should be provided as a string itself.

# We provided 'n' as the argument for .split() so our string “santana” got split at each 'n' character into a list of
# three strings.
greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a']

print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', '']

# Using .split() and the provided string, create a list called author_names containing each individual author name as
# it’s own string.
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala" \
          " Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

# Create another list called author_last_names that only contains the last names of the poets in the provided string.
author_last_names = []
for author_name in author_names:
  splited_author_name=author_name.split()
  author_last_names.append(splited_author_name[1])

print(author_last_names)

# 5.Splitting Strings III
# We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split by
# something in a string that is not necessarily a character. The two escape sequences we will cover here are
#
# \n Newline
# \t Horizontal Tab

# Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by tabs.


# 6.Joining Strings I

# 7.Joining Strings II
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

# 8.strip()


#11.format()
def poem_title_card(title,poet):
  return 'The poem "{}" is written by {}.'.format(title,poet)

poem_title_card("I Hear America Singing", "Walt Whitman")
