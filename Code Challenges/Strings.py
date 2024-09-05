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
