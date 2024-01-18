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