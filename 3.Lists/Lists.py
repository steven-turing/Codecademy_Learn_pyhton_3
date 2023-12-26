#1.What is a List?
#In Python, a list is one of the many built-in data structures that allows us to work with a collection of data in
# sequential order.
heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

#2.What can a List contain?
# Lists can contain more than just numbers.Lists can contain any data type in Python! For example, this list contains a
# string, integer, boolean, and float.
ints_and_strings = [1, 2, 3, "four", "five","True"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

#3.Empty Lists
#A list doesn’t have to contain anything. You can create an empty list like this:
my_empty_list = []

#4.List Methods
#For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go
# between the parenthesis of the method ( ).
example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)

#5.Growing a List: Append
#We can add a single element to a list using the .append() Python method.
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
print(orders)
orders.append("roses")
print(orders)

#6.Growing a List: Plus (+)
#When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = orders + ["lilac","iris"]
print(new_orders)

orders_combined = orders + new_orders
print(orders_combined)

broken_prices = [5, 3, 4, 5, 4] + [4]

#7.Accessing List Elements
