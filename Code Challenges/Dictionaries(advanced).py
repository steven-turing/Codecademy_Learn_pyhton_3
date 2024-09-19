# 1. Word Length Dict
# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
# Write your word_length_dictionary function here:
def word_length_dictionary(words): 
  dict = {}
  for word in words:
    dict[word] = len(word)
  return dict
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
# we can add the key and value to our dictionary using this syntax: word_lengths[word] = len(word).

# 2. Frequency Count
# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
#The function should return a dictionary containing the frequency of each element in words.

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  word_frequency = {}
  for word in words:
    if word in word_frequency.keys():
      word_frequency[word] += 1
    else:
      word_frequency[word] = 1
  return word_frequency
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#Here is how we solved it:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

# 3. Unique Values
# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the number of unique values in the dictionary.
# Write your unique_values function here:
def unique_values(my_dictionary):
  Unique = []
  for word in my_dictionary.values():
    if word not in Unique:
      Unique.append(word)
  return len(Unique)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# 4. Count First Letter
# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is 
# a last name and the value is a list of first names. For example, the dictionary might look like this:
# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for name in names:
      first_letter = name[0]
      if first_letter in letters:
         letters[first_letter] += len(names[name])
      else:
        letters[first_letter] = len(names[name])
  return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
# First letter extraction: The code uses first_letter = name[0] to extract the first letter of each key in the dictionary names.
# Dictionary initialization: Before adding to a key's value, we check if the key exists. If it exists, we increment the value. 
# If it doesn't, we initialize the key with the count from len(names[name]).

#Here is what we did:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
