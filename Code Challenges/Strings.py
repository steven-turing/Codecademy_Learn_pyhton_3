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


# This is how we solved it:
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4