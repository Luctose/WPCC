# WPCC
# functionEx1.py

# A useful thing in any programming language is being able to
# modularize parts of your program. We can accomplish this by
# defining our own functions

# We have seen functions before, like `print` and `randint`. These
# functions will do one thing, and one thing only. `print` will
# print stuff to the screen, `randint` will generate a random number
# given a range.

# We can design functions as well that will do a single task in our program

def myAddFunction(a, b):
    print("The sum is", a + b)

# Once we define the function, it must be 'called'
myAddFunction(9, 10)
myAddFunction(7, 5)

# We can define a function using `def` followed by the function's name. In the
# brackets, we have the "parameters" or "arguments" of the function. In `myAddFunction`,
# we have two arguments `a` and `b` that take on the values that are passed in
# when the function is called. For the first call, a=9 and b=10.
# For the second call, a=7 and b=5

# The naming scheme is the same as variables, as discussed in the assignment 1
# notes.


# The advantage of making functions is that we can use this function as many
# times as we want in our program without copy-pasting the code that
# sits inside it

# Say we have a function that has a fair amount of code in it:

def someLongFunction():
    a = 0
    b = 1
    while a < b:
        b += a
        if b % 100 == 0:
            b /= 2
        a += b
    print(a, b)

someLongFunction()

# This sizable function would be sort of annoying to use is multiple locations
# in our program:
x = 421
if x > 100:
    someLongFunction()

# But now we can call this long function wherever we want.


#########################
# EXERCISE
#########################

# Write a function called `reverse` that will take in a string
# and output the string in reverse. Then call the function with your
# name as a parameter
