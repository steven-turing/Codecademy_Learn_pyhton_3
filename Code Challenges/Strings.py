# Write a function called unique_english_letters that takes the string word as a parameter. The function should
# return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as
# different letters.
#
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to
# include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Write your unique_english_letters function here:
def unique_english_letters(word):
    num = 0
    counted_letter = ""
    for letter in word:
        if letter in letters:
            if letter not in counted_letter:
                counted_letter = counted_letter + letter
                num += 1
    return num


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Write a function named count_char_x that takes a string named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

# Write your count_char_x function here:
def  count_char_x(word, x):
  count = 0
  for a in word:
    if a == x:
      count += 1 
  return count
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.

#For example, count_multi_char_x("Mississippi", "iss") should return 2
# Write your count_multi_char_x function here:
def count_multi_char_x (word, x):
   splited_word = word.split(x)
   count = 0
   for num in splited_word:
      count += 1
   return count - 1
  
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#Here is one possible way to get the answer:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
