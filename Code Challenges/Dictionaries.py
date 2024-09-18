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

#
