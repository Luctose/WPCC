# WPCC
# fileioEx3.py

# Python is often used to "parse" data file because of it's ease of use when it comes
# to reading files, and also manipulating the strings after the data has been read.

# Parsing simply means to "sort through" and interpret data that sit in a file
# For example, we'll take a look at how to read a big file containing integers

# `nums.txt` contains 10,000 integers. I want to look at all of them, and find the
# average. Let's see how we can do this in Python

# First we open the file for reading
numFile = open('nums.txt', 'r')

# We can use the `split()` method to get a list of all the lines in the file
wholeFileString = numFile.read()
lines = wholeFileString.strip().split('\n') # The split function will take the string "wholeFileString"
                                            # and return a list, split by new line

# What's the difference between this and using the `readlines()` function? Well with `readlines()`, the returned
# list will contain the newline character at the end of each number, which is not what we want. We want
# only the numbers. We could've used `readlines()` and then deleted the '\n' from each element if we wanted,
# but I like this approach better


# Now we have a big list of numbers. Or do we? It turns out that when we read a file,
# the data is interpreted as a string by default. We know that all the numbers in the file
# are integers, but Python doesn't.

# Let's go through each number (i.e. each line) and make them into integers:

for i in range(len(lines)):
    lines[i] = int(lines[i])  # cast the string into an integer

# Now we can finally add up all the numbers and calculate the average
total = 0
for num in lines:
    total += num
avg = total / len(lines)

print(avg)

# Always remember to close the file when you're done with it
numFile.close()
