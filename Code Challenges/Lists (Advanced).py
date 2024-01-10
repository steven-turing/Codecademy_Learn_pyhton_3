# Coding question 1:Create a function called every_three_nums that has one parameter named start.
#
# The function should return a list of every third number between start and 100 (inclusive). For example,
# every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should
# return an empty list.
# Write your function here
def every_three_nums(start):
    every_three_nums_list = []
    while start <= 100:
        every_three_nums_list.append(start)
        start += 3
    return every_three_nums_list


# Uncomment the line below when your function is done
print(every_three_nums(91))


# Here is what we did:
# hint:range()
def every_three_nums(start):
    return list(range(start, 101, 3))
