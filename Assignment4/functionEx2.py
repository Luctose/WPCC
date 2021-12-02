# WPCC
# functionEx2.py

# When we call some Python standard functions, it gives us back
# a value that we can assign to a variable and use later in our programs.
# For example:

import random

randomNumber = random.randint(0, 10)

# This function will return the value it generates so we can assign its
# value to `randomNumber`

# So how can we do that in our own functions:
# Let's take a look at the function from the last note:

'''
def myAddFunction(a, b):
    print("The sum is", a + b)
'''

# This function will add the numbers, but we can't use it later in our
# program
'''
sum = myAddFunction(10, 5)
'''
# This will not give us the expected 15. `myAddFunction` will only print the sum,
# not return it

# So we can modify this function to return the value instead.

def myAddFunction(a, b):
    return a+b

theSum = myAddFunction(10, 20)
print(theSum)

# Our function now "returns" the value instead of printing it.
# This means that during runtime, the function call will take on the value
# that is returned:

# This is what it would look like behind the scenes:
'''
theSum = myAddFunction(10, 20)
theSum = .... compute
theSum = 20
'''

# Note: when a function reaches a `return` statement, it will terminate the whole
# function. For example:

def exFunc():
    return True
    print("PRINT ME PLS!!")

exFunc()
# The print will never happen because the function will have terminated
# at the return statement


#########################
# EXERCISE
#########################

# Write a function called `letterGrade()` that will take in
# a grade (integer) and return the appropriate letter grade

