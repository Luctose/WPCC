# WPCC
# functionEx4.py

# Now we're going to take a look at one of the more difficult
# concepts in Computer Science: recursion.

# Recursion is a way to solve problems that can be broken down into
# a lot of very similar problems. We make use of recursion by making
# recursive functions. A recursive function is a function in which
# the definition of said function involves calling itself!

# Let's take a look at a simple example:
# We can compute the sum of a list with a recursive approach.
# I could define the sum of a list as the following: "the sum of all elements inside the list"
# Then you would write a function that loops through every elements adds them up.
# But I could also define the sum of a list as: "The first element + sum of the rest of the elements"
# As you can see, I defined sum in terms of another sum; a smaller, but one-in-the-same sum.

# There are two things to consider when designing a recursive function:
# 1. The base case: The case where the recursive will *stop*. Usually it's when the problem
#       becomes small enough where we know the answer for sure.
# 2. The recursion: The case where you keep recursing *towards the base case*

# In the sum example, the base case would when our list is of length 1. In that case, we know the sum
# of that list: it's the element inside of it!

# So let's make this function

def mySum(some_list):
    # BASE CASE
    if len(some_list) == 1:
        return some_list[0] # The sum of a list of size 1 is just that element

    # RECURSIVE CASE
    # return: the first element + sum of the rest of the list
    return some_list[0] + mySum(some_list[1:])

# Let's see of this works:
print(mySum([10, 20, 30, 40]))

# If you run this program, it will indeed print the expected 100

# So let's trace this program to see what's happening:
'''
  mySum([10, 20, 30, 40])             # Starting point
= 10 + mySum([20, 30, 40])            # recurse
= 10 + ( 20 + mySum([30, 40]) )       # recurse
= 10 + ( 20 + ( 30 + mySum([40]) ) )  # recurse
= 10 + ( 20 + ( 30 + 40 ) )           # base case
= 10 + ( 20 + 70 )                    # compute
= 10 +  90 
= 100
'''


#########################
# EXERCISE
#########################

# Write a recursive function called `factorial` that
# will take in an integer, and compute its factorial.

# Hint: 6! = 6 * 5!

