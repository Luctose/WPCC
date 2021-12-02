# WPCC
# loopsEx1.py


# As of now you have learned print statements, basic arithmetic, and some
# string formatting. These notes will introduce you to loops.

# Loops are used when executing something with repetition
# instead of typing out the specific statement or command
# over and over again.
# In Python, there are two types of loops:
# "for" loops and "while" loops


# For loops are usually used when you know how many times
# some block of code is going to be executed; whereas while
# loops are usually used when you don't know exactly how many
# iterations to run a block of code

# To make a for loop in Python, you need to declare some things:
# a variable(s) that will change during the duration of the loop,
# and a set of values this variable will take on.

for some_var in range(10):
    print("Printing for the %d time" % some_var)
# Note: INDENTATION IS VERY IMPORTANT

# This "for" loop will loop 10 times total. During each iteration,
# the variable `some_var` will take on different values. Looking
# at the output of the program, we can see that `some_var` takes on
# the value 0, then 1, 2, 3, 4... and so on until 9.

# This is thanks to this new function called `range`.
# The `range` function can be called with a different number of arguments.

for i in range(20, 30):
    print("I'm", i, "years old")

# If two arguments are given to `range`, the first value is the "start" number,
# and the second value is the "end" value. This loop will start at 20, and iterate
# until i=29, one less than the second argument


# Say we give 3 values to range:
for k in range(7, 14, 3):
    print(k)
# This example, the third value represents the "step."
# It will start with k=7, and add 3 after every iteration.
# So, `k` will take on the values 7,10,13. After that, the value of `k`
# will exceed the second value (14), causing the for loop to exit

#########################
# EXERCISE
#########################

# Write a Python program that will generate 100 random numbers between 420 (inclusive)
# and 690 (inclusive) and print them.

