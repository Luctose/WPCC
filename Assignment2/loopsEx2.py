# WPCC
# loopsEx2.py

# There are operations we can do to "strings" that are special to
# this data type

# One of these operations is called indexing: we can extract
# portions of a string by giving Python some information
# on what we want to extract:

a_cool_str = "What a wonderful world"
print(a_cool_str[0]) # Prints 'W'

# We can use this syntax to tell Python to only extract the very
# first character from this string. Notice that to get the first
# character in a string, we tell Python we want character 0.
# This is because Python, much like other languages, starts indexing
# at 0.

# Say we want to extract just the 3rd word. We can tell Python to
# get a portion of the original string, from the 8th character until
# the 16th character. Since Python indexes strings starting at 0,
# we start at index 7. But we go until index 16, not 15. This is because
# Python will go up until the second index specified, BUT NOT INCLUDING IT.

print(a_cool_str[7:16])      # wonderful

# Say we want to get the original string, but with just the first character
# removed. We can use the above notation, but not specify an end index:

print(a_cool_str[1:])        # hat a wonderful world

# This will take the string starting at index 1 (2nd character) and go
# until the end of the string.



# Now where do loops come into this? We can use loops to iterate
# through strings. In the last example, we looked at the `range` command.
# We can tell Python to loop through all indices in a string like this:

for index in range(len(a_cool_str)):
    print(index, a_cool_str[index])

# With the help of the `len` function, we can loop through
# all the indices of `a_cool_str`: from 0 until 21. The `len`
# will tell us the length of a string, and we can use that
# as a parameter for the `range` function

#########################
# EXERCISE
#########################
# Write a Python program that makes a variable with value: "illiosvsewpcyttvhxozn"
# With the help of the `range` function, print every other letter
# of the string, starting at index 0

word = "illiosvsewpcyttvhxozn"
