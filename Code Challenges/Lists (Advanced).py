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


# Coding question 2:Create a function named remove_middle which has three parameters named my_list, start, and end.
#
# The function should return a list where all elements in my_list with an index between start and end (inclusive)
# have been removed.
#
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:
#
# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
# Write your function here
def remove_middle(my_list, start, end):
    return my_list[:start] + my_list[end + 1:]


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# Coding question 3:Create a function named more_frequent_item that has three parameters named my_list, item1,
# and item2.
#
# Return either item1 or item2 depending on which item appears more often in my_list.
#
# If the two items appear the same number of times, return item1.
# Write your function here
def more_frequent_item(my_list, item1, item2):
    if my_list.count(item1) >= my_list.count(item2):
        return item1
    else:
        return item2


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Coding question 4:Create a function named double_index that has two parameters: a list named my_list and a single
# number named index.
#
# The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.
#
# If index is not a valid index, the function should return the original list.
#
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
#
# double_index([1, 2, 3, 4], 2)
# Write your function here
def double_index(my_list, index):
    if 0 <= index <= len(my_list):
        my_list[index] = my_list[index] * 2
        return my_list
    else:
        return my_list


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


# Here is one way to do it:
def double_index(my_list, index):
    # Checks to see if index is too big
    if index >= len(my_list):
        return my_list
    else:
        # Gets the original list up to index
        my_new_list = my_list[0:index]
    # Adds double the value at index to the new list
    my_new_list.append(my_list[index] * 2)
    #  Adds the rest of the original list
    my_new_list = my_new_list + my_list[index + 1:]
    return my_new_list


print(double_index([3, 8, -10, 12], 2))


# Coding question 5:Create a function called middle_element that has one parameter named my_list.
#
# If there are an odd number of elements in my_list, the function should return the middle element. If there are an
# even number of elements, the function should return the average of the middle two elements.
# Write your function here
# hint: TypeError: list indices must be integers or slices, not float
# my_list[int(len(my_list)/2) - 1]
def middle_element(my_list):
    if len(my_list) % 2 == 1:
        return my_list[int(len(my_list) / 2)]
    elif len(my_list) % 2 == 0:
        return (my_list[int(len(my_list) / 2) - 1] + my_list[int(len(my_list) / 2)]) / 2


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
