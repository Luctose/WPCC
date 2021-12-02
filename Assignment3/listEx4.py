# WPCC
# listEx4.py

import random

# Another important function in lists is randomizing the order
# of the elements:

some_numbers = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

random.shuffle(some_numbers)

print(some_numbers)

# As we can see from the print, `some_numbers` has been randomized
# *IN PLACE*. So that means that our original list is lost.

# What if we want to keep our original list, but shuffle it and store
# it in another variable:

list1 = [4, 8, 15, 16, 23, 42]

# First, we copy it
list2 = list1[:]
# We are getting the sub list of `list1` from the beginning until the end.
# Internally, Python will create a new list and copy every element into it

# Now we can shuffle it
random.shuffle(list2)
print(list2)

# Now we have the original `list1` as well as a shuffled `list2`

#########################
# EXERCISE
#########################

# Write a program that makes a list of numbers. Then create a copy of the
# list and shuffle it. Then print out the difference between their indices
# from the original list and the new shuffled list:

# example: original_list = [1, 2, 3, 4, 5]
#          shuffled_list = [4, 3, 5, 1, 2]

# output:
# difference of element 1: 3
# difference of element 2: 3
# difference of element 3: -1
# difference of element 4: -3
# difference of element 5: -2

original_list = [1, 2, 3, 4, 5]



