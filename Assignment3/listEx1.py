# WPCC
# listEx1.py

# In this section, we will take a look at lists in Python.

# Lists are used to store variable amounts of data. A list
# is defined using square brackets:

a_list = []

# We just created an empty list, stored in the variable a_list

# But an empty list is kind of useless... So let's put some values into it:

a_list.append(2)
a_list.append(30)
a_list.append(-19)

# We just added 3 integer values into this list. Like with variables, we
# don't need to define what type of values this list will be holding.


# We can even store more than 1 type of value into this list:

a_list.append('Some string value')
a_list.append(True)

# To see the contents of this list, we can just pass it into `print`

print(a_list)


# If you know exactly what values you need to put in a list,
# you can define it in one step:

another_list = ["pizza", "pasta", "chicken noodle soup"]

# We can put our data in a list by typing them in between the square
# brackets, separated by a comma

print(another_list)

#########################
# EXERCISE
#########################

# Write a Python program that makes a list with 10 numbers.
# Then compute the sum of the list and output it.




