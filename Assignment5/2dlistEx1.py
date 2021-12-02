# WPCC
# 2dlistEx1.py

# We're going to look at what a 2D list is.
# A 2D list is a list that contains other lists.

# For example:
marks = [ [90, 85, 88], [68, 73, 79] ]
# The list `marks` contains 2 other lists, each containing
# integers. We would say that this list is of size 2x3:
# two lists, each containing 3 elements

print(len(marks)) # This will print how many lists are in `marks`
print(len(marks[0])) # This will print how many elements are in the first list inside `marks`


# So why would we want to create something like this?
# In some problems, we need to model something like a grid
# or board that requires 2 coordinates or 2 indices. For example,
# in a game of chess a piece's location is represented with 2 values:
# a row position and a column position. We can model a chess board using
# a 2D list

board = [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

# The `board` list contains 8 other lists, each containing 8 numbers. (8x8)
# This above list has a 1 in the first list at the sixth index.

# The way we would access that element is by first taking the index of the
# list, then the index of the element inside of that list.

# So to get the 7th element in the 1st list:
print( board[0][6] ) # This will print `1`

# Notice that each list the same length. In Python, it's not necessary to keep
# all lists the same length, but it's definitely easier (as we've seen before, Python
# can work with different kinds of data). In other programming languages,
# making a 2D list with different list sizes would not be possible.


#########################
# EXERCISE
#########################

# Write a Python program that creates a 3x3 2D list of ints.
# Then print out the middle element i.e. The element in the 2nd list, at the 2nd spot


