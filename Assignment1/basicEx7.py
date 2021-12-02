# WPCC
# basicEx7.py

# Let's take a look at how we can print multiple pieces of data
# in 1 print statement

# We will use something called "string formatting"
# For example, say we want to print a number in the middle of a
# sentence

print( "The number %d is a cool number" % 69 )
#                  ^                    ^
# The "%d" inside the string is called the 'format specifier.' This
# format specifier *specifies* that an integer be inserted into
# that spot in the string. The '%' means that we want to format the value
# following it into the string preceding it.

# Here is a list of all format specifiers and their corresponding types

# %s - str
# %d - int/bool
# %f - float

# But more can be done with string formatting. We can specify the field
# size of a format specifier. Say we want to print a string in a field size
# of 20 characters

print("Here it is:|%20s|" % "python")
# This will print:

"""
    Here it is:|              python|
"""

# As we can see, the python has been formatted "python" between the '|' characters
# within 20 spaces (including the actual string to be formatted).
# Also note that the data is RIGHT aligned

# We can specify the field size for any of the format specifiers:
print("%30d" % 420)
print("%30s" % "Is the best number")
print("%-30f" % 72.8)

# We put a negative value for the last print statement. This is not an error,
# it causes the value to be LEFT aligned

# What happens if the data we give is more than the field size we specify?

print("%10s" % "This is a very very very very long sentence")

# this prints:  "This is a very very very very long sentence"
# The data that exceeds 10 characters is not cut off, but is instead
# printed in its entirety


# How would we format multiple values into the same string?
# Say we have the (x,y) values of an ordered pair:

print( "The values of the coordinates are: x=%d y=%d" % (24, 6) )
# Note: if we supply more than 1 value, we must put brackets around all the values
# we are going to format

#########################
# EXERCISE
#########################

# Write a python program that prints a nicely formatted table
# of names and ages. Put in 3 different names and ages:
# Note: names column should be left aligned spanning 30 characters,
#       the age column should be right aligned spanning 10 characters

# SAMPLE:
'''
Name                          |       Age
John                          |        17
Trinity                       |        15
Jacob                         |         2
'''


