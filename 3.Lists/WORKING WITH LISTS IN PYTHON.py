# 1.Working with Lists
# Now that we know how to create and access list data, we can start to explore additional ways of working with lists.
#
# In this lesson, you’ll learn how to:
#
# Add and remove items from a list using a specific index.
# Create lists with continuous values.
# Get the length of a list.
# Select portions of a list (called slicing).
# Count the number of times that an element appears in a list.
# Sort a list of items.

# 2.Adding by Index: Insert
# The Python list method .insert() allows us to add an element to a specific index in a list.

# The .insert() method takes in two inputs:
# The index you want to insert into.
# The element you want to insert at the specified index.
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0, "Pineapple")
print(front_display_list)

# 3.Removing by Index: Pop
# The .pop() method takes an optional single input:
# The index for the element you want to remove.
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

# 4.Consecutive Lists: Range
# The function range() takes a single input, and generates numbers starting at 0
# and ending at the number before the input.
number_list = range(9)
# print(number_list)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# 5.The Power of Range!
# By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list
# that starts at a different number.

# If we use a third input, we can create a list that “skips” numbers.
range_five_three = range(5, 15, 3)

range_diff_five = range(0, 40, 5)

# 6.Length
# Often, we’ll need to find the number of items in a list, usually called its length.
# We can do this using a built-in function called len().
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice",
             "getting", "the", "length"]

big_range = range(2, 3000, 10)

long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

big_range = range(2, 3000, 100)
print(len(big_range))

# 7.Slicing Lists I
# In Python, often we want to extract only a portion of a list.
# Dividing a list in such a manner is referred to as slicing.
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]
print(beginning)

beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

# 8.Slicing Lists II
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# 9.Counting in a List
# If we want to know how many times i appears in this word, we can use the list method called .count():
# We can even use .count() to count element appearances in a two-dimensional list.
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake",
         "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below:
jake_votes = votes.count("Jake")
print(jake_votes)

# 10.Sorting Lists I
# We can sort a list using the method .sort().
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace",
             "1600 Pennsylvania Ave", "10 Downing St."]

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()

# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()

addresses.sort()
print(addresses)

print(sorted_cities)

cities.sort(reverse=True)
print(cities)

# 11.Sorting Lists II
# A second way of sorting a list in Python is to use the built-in function sorted().
#
# The sorted() function is different from the .sort() method in two ways:
#     It comes before a list, instead of after as all built-in functions do.
#     It generates a new list rather than modifying the one that already exists.
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games)
print(games_sorted)

# 12.Review
# Add elements to a list by index using the .insert() method.
# Remove elements from a list by index using the .pop() method.
# Generate a list using the range() function.
# Get the length of a list using the len() function.
# Select portions of a list using slicing syntax.
# Count the number of times that an element appears in a list using the .count() method.
# Sort a list of items using either the .sort() method or sorted() function.

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table",
             "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow",
             "pillow"]

inventory_len = len(inventory)

first = inventory[0]

last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory.pop(4)

inventory.insert(10, "19th Century Bed Frame")
print(inventory)

sorted = sorted(inventory)
print(inventory)
print(sorted)

inventory.sort()
print(inventory)

