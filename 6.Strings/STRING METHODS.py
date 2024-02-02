# Lesson 2 Strings Methods
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
    splited_author_name = author_name.split()
    author_last_names.append(splited_author_name[1])

print(author_last_names)

# 5.Splitting Strings III
# We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split by
# something in a string that is not necessarily a character. The two escape sequences we will cover here are
#
# \n Newline
# \t Horizontal Tab

# Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by
# tabs.

# Create a list called spring_storm_lines that contains a string for each line of Spring Storm
spring_storm_text = \
    """The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

# 6.Joining Strings
# Let’s learn to put them back together using .join(). .join() is essentially the opposite of .split(), it joins a list
# of strings together with a given delimiter.The syntax of .join() is:'delimiter'.join(list_you_want_to_join)
# We take the list of strings and we joined it together with our delimiter, ' ', which is a space.
# The space is important if you are trying to build a sentence from words.

# Use .join() to combine these words into a sentence and save that sentence as the string reapers_line_one.
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

# 7.Joining Strings II
# In fact, you can use any string as a delimiter to join together a list of strings.
# One often used string is a comma , because then we can create a string of comma-separated values, or CSV.
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# You can also join using escape sequences as the delimiter.
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio',
                            'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)

# You’ve been given a list, winter_trees_lines, that contains all the lines to William Carlos Williams poem,
# Winter Trees. You’ve been asked to join together the strings in the list together into a single string that can be
# used to display the full poem. Name this string winter_trees_full.
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!',
                      'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds',
                      'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# 8.strip()
# When working with strings that come from real data, you will often find that the strings aren’t super clean. You’ll
# find lots of extra whitespace, unnecessary linebreaks, and rogue tabs.
# Python provides a great method for cleaning strings: .strip(). Stripping a string removes all whitespace characters
# from the beginning and end.

# Consider the following example:
featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas' All the whitespace on either side of the string has been stripped, but the whitespace in the middle
# has been preserved.

# You can also use .strip() with a character argument, which will strip that character from either end of the string.
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       ' By including the argument '!' we are able to strip all of the ! characters from either side
# of the string. Notice that now that we’ve included an argument we are no longer stripping whitespace, we are ONLY
# stripping the argument.

# They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. They want you to join
# together all of the lines into a single string that can be used to display the poem again, but this time,
# you’ve noticed that the list contains a ton of unnecessary whitespace that doesn’t appear in the actual poem.
#
# First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list
# love_maybe_lines_stripped.
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

print(love_maybe_lines_stripped)

# .join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be
# printed to display the poem.
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# 9.Replace
# The next string method we will cover is .replace(). Replace takes two arguments and replaces all instances of the
# first argument in a string with the second argument. The syntax is as follows
# string_name.replace(substring_being_replaced, new_substring)

# The poetry organization has sent over the bio for Jean Toomer as it currently exists on their site. Notice that
# there was a mistake with his last name and all instances of Toomer are lacking one o.
#
# Use .replace() to change all instances of Tomer in the bio to Toomer. Save the updated bio to the string
# toomer_bio_fixed.
toomer_bio = \
    """Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, 
    D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham 
    County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of 
    African-Americans in southern farmlands. """

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

# 10.find()
# Another interesting string method is .find(). .find() takes a string as an argument and searching the string it was
# run on for that string. It then returns the first index value where that string is located.
# Here’s an example:
print('smooth'.find('t'))
# => '4'

# At what index place does the word “disown” appear? Save that index place to the variable disown_placement.
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

print(disown_placement)


# 11.format()
# Python also provides a handy string method for including variables in strings. This method is .format().
# .format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as
# placeholders for where those variables will be imported.

# Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet.
# The function should use .format() to return the following string: The poem "[TITLE]" is written by [POET].
# For example, if the function is given the inputs
#
# poem_title_card("I Hear America Singing", "Walt Whitman")
#
# It should return the string
#
# The poem "I Hear America Singing" is written by Walt Whitman.

def poem_title_card(title, poet):
    return 'The poem "{}" is written by {}.'.format(title, poet)


poem_title_card("I Hear America Singing", "Walt Whitman")


# 12.format() II
# .format() can be made even more legible for other people reading your code by including keywords.
# Previously, with .format(), you had to make sure that your variables appeared as arguments in the same order that you
# wanted them to appear in the string, which added unnecessary complications when writing code.
# By including keywords in the string, and in the arguments, you can remove that ambiguity.

#  Let’s look at an example.
def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)


# if the arguments of .format() are in a different order, the code will still work since the keywords are present:
def favorite_song_statement(song, artist):
    # this will have the same output as the above example
    return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)


# The function poem_description is supposed to use .format() to print out some quick information about a poem
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        title=title, author=author, original_work=original_work, publishing_date=publishing_date)
    return poem_desc


my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)

# 13，Review
# Over this lesson you’ve learned:
#
# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() allows you to interpolate a string with variables.
# Well I’ve been stringing you along for long enough, let’s get some more practice in!

# 1.Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems,
# titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into
# something that can display the name, title, and publication date of the highlighted poems on the site.
#
# First, start by printing highlighted_poems to the terminal and see how it displays.
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela " \
                    "Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold " \
                    "Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico " \
                    "City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, " \
                    "Dreamwood:Adrienne Rich:1987 "

print(highlighted_poems)

# 2.The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.
#
# Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.
# Print highlighted_poems_list, how does the structure of the data look now?
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

# 3.Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.
# Print highlighted_poems_stripped.
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)

# 4.Next we want to break up all the information for each poem into it’s own list
# Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into
# highlighted_poems_details.
highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
print(highlighted_poems_details)

# 5.Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.
# Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists
# titles, poets, and dates.Finally, write a for loop that uses .format() to print out the following string for each poem:
# The poem TITLE was published by POET in DATE.
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  print("The poem {} was published by {} in {}.".format(poem[0],poem[1],poem[2]))

