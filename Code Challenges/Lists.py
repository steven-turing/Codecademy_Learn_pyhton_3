# Coding question 1 ：Create a function called append_size that has one parameter named my_list.
#
# The function should append the size of my_list (inclusive) to the end of my_list. The function should then return
# this new list.
#
# For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list
# was originally 3.
# Write your function here
def append_size(my_list):
    my_list.append(len(my_list))
    return my_list


# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


# Coding question 2 ：Write a function named append_sum that has one parameter — a list named named my_list.
#
# The function should add the last two elements of my_list together and append the result to my_list. It should do
# this process three times and then return my_list.
#
# For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
# Write your function here
def append_sum(my_list):
    my_list.append(my_list[-1] + my_list[-2])
    my_list.append(my_list[-1] + my_list[-2])
    my_list.append(my_list[-1] + my_list[-2])
    return my_list


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


# Coding question 3 ：Write a function named larger_list that has two parameters named my_list1 and my_list2.
#
# The function should return the last element of the list that contains more elements. If both lists are the same
# size, then return the last element of my_list1.
# Write your function here
def larger_list(my_list1, my_list2):
    if len(my_list1) > len(my_list2):
        return my_list1[-1]
    elif len(my_list1) < len(my_list2):
        return my_list2[-1]
    else:
        return my_list1[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# Here is how we did it:

def larger_list(my_list1, my_list2):
    if len(my_list1) >= len(my_list2):
        return my_list1[-1]
    else:
        return my_list2[-1]


# Coding question 4 ：Create a function named more_than_n that has three parameters named my_list, item, and n.
#
# The function should return True if item appears in the list more than n times. The function should return False
# otherwise.

# Coding question 5 ：Create a function named more_than_n that has three parameters named my_list, item, and n.
#
# The function should return True if item appears in the list more than n times. The function should return False
# otherwise.

# In order to easily count the number of occurrences of item in my_list we can use the count() function.
def more_than_n(my_list, item, n):
    if my_list.count(item) > n:
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
