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
