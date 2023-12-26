# 1.What is a List?
# In Python, a list is one of the many built-in data structures that allows us to work with a collection of data in
# sequential order.
heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

# 2.What can a List contain?
# Lists can contain more than just numbers.Lists can contain any data type in Python! For example, this list contains a
# string, integer, boolean, and float.
ints_and_strings = [1, 2, 3, "four", "five", "True"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

# 3.Empty Lists
# A list doesn’t have to contain anything. You can create an empty list like this:
my_empty_list = []

# 4.List Methods
# For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go
# between the parenthesis of the method ( ).
example_list = [1, 2, 3, 4]

# Using Append
example_list.append(5)
print(example_list)

# Using Remove
example_list.remove(5)
print(example_list)

# 5.Growing a List: Append
# We can add a single element to a list using the .append() Python method.
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
print(orders)
orders.append("roses")
print(orders)

# 6.Growing a List: Plus (+)
# When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = orders + ["lilac", "iris"]
print(new_orders)

orders_combined = orders + new_orders
print(orders_combined)

broken_prices = [5, 3, 4, 5, 4] + [4]

# 7.Accessing List Elements
# In Python, we call the location of an element in a list its index.
# Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.
# We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted
# to select the third element from the list, we’d use calls[2]:print(calls[2])
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employee_four)

print(employees[0])

# 8.Accessing List Elements: Negative Index
# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]

index5_element = shopping_list[5]

print(index5_element)
print(last_element)

# 9.Modifying List Elements
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# 10.Shrinking a List: Remove
# We can remove elements in a list using the .remove() Python method.
# We can also use .remove() on a list that has duplicate elements.
# Only the first instance of the matching element is removed:
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list)

new_store_order_list.remove("Onions")

# 11.Two-Dimensional (2D) Lists
# Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]

heights.append(["Vik", 68])
print(heights)

ages = [["Aaron", 15], ["Dhruti", 16]]
print(ages)

# 12.Accessing 2D Lists
# Instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first.
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

# 13.Modifying 2D Lists
incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# 14.Review
# So far, we have learned:
# How to create a list
# How to access, add, remove, and modify list elements
# How to create a two-dimensional list
# How to access and modify two-dimensional list elements
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True],
                 ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False

customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)
