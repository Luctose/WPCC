# WPCC
# listEx3.py

# If we have the following list:
names = ['Miles', 'Finley', 'Miranda', 'Roy', 'Will', 'George']

# What if we want to find the index at which some element sits?
# For example, I want to know which index 'Roy' is at

print("'Roy' is at index", names.index('Roy'))

# The `index` function will search the list `names` and tell
# us where 'Roy' is located

# Say we search for something not in the list:

"""
print("'Sandy' is at index", names.index('Sandy'))
"""
# This will give an error, saying "Sandy" is not in the list
# So how can we avoid this error? We can test if the name is in the list
# first, then get the index:

if 'Sandy' in names:
    print("'Sandy' is at index", names.index('Sandy'))
else:
    print("'Sandy' is not in the list")



# Let take a look at how to sort a list.
# When sorting a list of string, it will sort the elements alphabetically

names.sort()

# The `sort` function will sort names *IN PLACE*. That means that the original
# list will be modified and sorted. So if we needed the original permutation
# of the list, it is lost.

print(names)

# As we can see, the original list has changed and has indeed been sorted

#########################
# EXERCISE
#########################

# Write a Python program that makes a list of names like `names` above and
# reverse every single string in the list. Then sort the new list of reversed names
# and print it out

names = ['Miles', 'Finley', 'Miranda', 'Roy', 'Will', 'George']




