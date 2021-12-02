# WPCC
# basicEx2.py

# Let's take a look at some different types of data that Python
# knows about:

print(10)
print(3.14)
print("Python is awesome!")
print(True)

# There are 4 fundamental types of data in Python:
# integers, floating point numbers, strings, and booleans
# You can create more types of data, but we'll examine those
# later on.

# You can declare a "variable" like this in Python:

x = 54

# This variable is of the type "int"
# We can see this by running the "type" function:
print(type(x))

# this prints: <class 'int'>
# Python will interpret this variable as an integer number

# We can also make variables of type `float`
y = 5.43
print(type(y))   # <class 'float'>
# This type of data will store fractional numbers

# The next data type is called a string. This data type will hold
# a sequence of characters, and by doing so can store pretty much all
# kinds of different data like names, colors, addresses etc. A string can
# be defined with single quotes ('') or double quotes ("").

# Be careful as strings can also store numbers, and numbers stored
# in string ARE NOT # the same as their equivalent integer or float forms:

a_number = '13'     # <class 'str'>
another_number = 13

# NOTE PYTHON DOESN'T SEE THESE VARIABLES AS THE SAME THING.
# One will hold the sequence of characters: '1', and '3'
# The other is the integer representation of the number 13

# Lastly, we have booleans. This type of data can only take on two different
# values: true, or false. When making booleans in Python, you must capitalize
# the first letter: True/False
a_bool = True
another_bool = False
print(type(a_bool))  # <class 'bool'>




# When declaring a variable, you must follow some rules with its name:
# the name may contain lowercase/uppercase letters and as well as numbers,
# but the first character must NOT be a number.

"""
50cent = "the best"
"""

# THIS IS NOT A VALID VARIABLE. (put a "#" on the previous line to run this file)

# but this is:
w20_e3j = True

# Be careful when referring to an existing variable, VARIABLES ARE CASE SENSITIVE
# `variable_with_good_name` IS NOT THE SAME AS `Variable_with_good_name`

print(x)
x = 2.71

# We can reassign the same variable to a different type,
# and Python won't care. In other programming languages,
# this is NOT allowed. But Python doesn't care, it's different!

# Python is smart, and will automatically convert between different
# types if needed. For example, let's try to divide a floating
# point number by an integer

some_number = 10.5
some_other_number = 2
print(some_number / some_other_number)

# The answer is 5.25 (type is `float`). In other languages, the different types
# would not play well together, but as I mentioned before, Python is smart


#########################
# EXERCISE
#########################

# Write a python program that makes a variable of every type mentioned in this file.
# Then print out their values

