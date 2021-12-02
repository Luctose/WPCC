# WPCC
# basicEx5.py

# Let's look at how to generate random numbers in Python
# We will have to import a Python library for this functionality

import random

# This will import the "random" library so we can use it's functions
# in this file. Whenever we use functions that has been defined in
# the random library, we will to use a special syntax:

print( random.randint(20, 30) )

# The `randint` function that is defined in the random library
# will generate a random integer between two numbers that we give
# to it. 

# We can even assign this value to a variable:

some_random_number = random.randint(1, 100)

# `some_random_number` will contain a random number from 1 to 100 (inclusive)
# We won't know what this number is until we run the program, but sometimes
# this is behaviour that we want in our program

# The random library also provides more functions. We will visit them
# later on in the course


#########################
# EXERCISE
#########################
# Write a python program that has a 1/10 chance to print "Hello World!"

