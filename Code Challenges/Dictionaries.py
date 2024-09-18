# 1. Sum Values
# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary

# Write your sum_values function here:
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# 2. Even Keys
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, 
# as a parameter. This function should return the sum of the values of all even keys.
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum = 0
  for key in  my_dictionary.keys():
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# 3. Add Ten
# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
# The function should add 10 to every value in my_dictionary and return my_dictionary

# Write your add_ten function here:
def add_ten(my_dictionary ):
  for key in  my_dictionary.keys():
    my_dictionary[key] += 10
  return  my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# 4. Values That Are Keys
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
# This function should return a list of all values in the dictionary that are also keys.

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  list = []
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if key == value:
        list.append(key)
  return list
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#Here is this solution:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys
