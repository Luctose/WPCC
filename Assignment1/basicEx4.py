# WPCC
# basicEx4.py

# So far, the out Python programs have been running from top to bottom:
# every line that's not in comments has been executed by Python.
# But what if we wanted Python to make a decision? To only
# run some code if a condition is met

# That's where we use if statements:

x = 10

if x > 20:
    print("x is greater than 20!")

# This is the first time we see a "code block". In python, spacing is VERY important
# to distinguish what code belongs inside the `if` statement, and what remains outside

# This:
if x > 20:
    print("x is greater than 20!")
# is NOT the same as this:
if x > 20:
    print("x is greater than 20!")

# The latter will result in an error because Python expects you to indent the code that
# is inside the if statement.

# The `if` keyword is used to do comparison operations between
# different values. The above will check if the value of `x` is
# greater than 20.

y = 17

# Conditionals can do different checks:
print(x > y) # True if x is greater than y
print(x >= y) # True if x is greater or equal to y
print(x < y) # True if x is less than y
print(x <= y) # True if x is less or equal to y
print(x == y) # True if x equals y

# Notice that to check if x has to same value as y, we use double equals, not single equal.
# This is because when Python sees a single equal, it thinks you're trying to assign
# a new variable, not check equality.

# As we can see in this case, x is NOT greater than 20. We can use the `else`
# keyword to catch every other case that doesn't fall into the `if` statement's
# condition:

if x > 20:
    print("x is greater than 20!")
else:
    print("x is less than or equal than 20!")

# Say we want to check two different cases: x is greater than 20, x is between
# 10, and 20, and every other case. We can use the `elif` keyword (short for "else if"):

if x > 20:
    print("x is greater than 20!")
elif 10 < x <= 20:
    print("x is between 10 and 20!")
else:
    print("every other case")

# Python will check the very first condition. If it is met,
# the rest of the conditions are skipped. Python will completely
# ignore the `elif` and `else` blocks of code.


#########################
# EXERCISE
#########################

# Write a python program that will make two strings, and check if they are equal to
# each other. If they are, print "They're equal!"
# Otherwise, print "They're not equal!"

