# Coding question 1. Tenth Power
# Write a function named tenth_power() that has one parameter named num.
#
# The function should return num raised to the 10th power.
# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# Coding question 2.Square Root
# Write a function named square_root() that has one parameter named num.
#
# Use exponents (**) to return the square root of num.
#
# Hint
# Write your square_root function here:
def square_root(num):
  return num ** 0.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# Coding question 3.Win Percentage
# Create a function called win_percentage() that takes two parameters named wins and losses.
#
# This function should return out the total percentage of games won by a team based on these two numbers.

# Write your win_percentage function here:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# Coding question 4.Average
# Write a function named average() that has two parameters named num1 and num2.
#
# The function should return the average of these two numbers.
# Write your average function here:
def average(num1, num2):
  return (num1 + num2)/2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# Coding question 5.Remainder
# Write a function named remainder() that has two parameters named num1 and num2.
#
# The function should return the remainder of twice num1 divided by half of num2.
# Write your remainder function here:
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
