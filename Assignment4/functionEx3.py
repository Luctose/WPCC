# WPCC
# functionEx3.py

# Let's take a look at how a function may return more
# than one value.

# As we saw in the last note, the function will exit when it
# encounters a `return` statment. So obviously we can't return
# twice with two different values. But what we can do is return
# a list containing the values we wish to return.

# When would we need to do something like this?
# Say we make a function that will compute the roots/x-intercepts
# of a quadratic equation, given `a`, `b`, and `c`

# We'll take the help of the `math` library, which will provide the `sqrt` function
import math
def computeRoots(a, b, c):
    d = math.sqrt(b*b - 4*a*c)

    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)

    return [x1, x2]

print(computeRoots(5, 7, 0))

# This will print both roots of 5x^2 + 7x.

# You know what would make this function even better than
# how it is right now? If I didn't have to supply the `c`
# value. What if we didn't supply it, it defaulted to c=0?

def computeRoots(a, b, c=0):
    d = math.sqrt(b*b - 4*a*c)

    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)

    return [x1, x2]

print(computeRoots(5, 7))
print(computeRoots(-6, -2, 69))

# Here we have the same function, but the last argument is optional.
# If it's not provided, the function continues with c=0. But you can
# still pass in a `c` value like we had before.

# I can have a function have as many optional arguments as I want.

def add(a, b, c=0, d=0, e=0, f=0, g=0, h=0):
    return a+b+c+d+e+f+g+h

print(add(1, 2, 3, 4))
print(add(69, 420))

# Say I want to supply a value of 4 for `g`, but not for c,d,e,f?
# We can explicitly say g=4

print(add(1, 2, g=4))

# As it turns out, we have been using a function that has had optional arguments
# all this time: `print`

print("Winter", "Python", "Code", "Camp")
# By default, print will print these strings with a single space between them.
# That can be changed:
print("Winter", "Python", "Code", "Camp", sep='-')
# We can optionally provide a separator value. Now this will print "Winter-Python-Code-Camp"

#########################
# EXERCISE
#########################

# Write a function called `myPrint` that mimics the print function. It will take in a list, and optionally
# a `sep` and `end` value (defaults to ' ' and '\n' respectively). Then loop through the list and print all the values with
# `sep` value between them. Then at the end of the list, print out the `end` string


