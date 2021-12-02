# WPCC
# listEx5.py

# Being able to navigate a list is very important. Being able to store a big list
# of items would be pretty useless if we had to access them one by one. So we
# will use loops to 'visit' every item in our list

# Say we have the following list:
nums = [43, 28, 39, 10, 49, 33, 17, 26, 45, 20]

# I want to add 10 to every number in this list. We could do it one by one:
'''
nums[0] = nums[0] + 10
nums[1] = nums[1] + 10
...
'''
# But what's the use of that? We might as well not use a list at this point.
# So there must be a better way of going through every element in this list
# and performing the same task:

# That's where loops come into play. We can use a `for` loop to iterate through every
# index in this list. We need to generate a loop that goes from 0 until the length of the list:

for i in range(len(nums)):
    nums[i] = nums[i] + 10
    print(nums[i])

# Recall: if one 'argument' is passed into the `range` function, it starts the loop at i=0.

# Like with strings, the `len` function can be used to get the length of a list. This
# loop will start with i=0, and add 10 to the '0th' element of the list, then add 10 to the '1st' element,
# and so on. Note that in this loop, we are looping through the *indices* of the list. This kind of loop
# is usually used when the indices are important in the operation we wish to do on the list.
# In this case we needed the index to assign the new value (nums[i]+10) back to the list.


# We can also loop explicitly through the elements in a list:
for n in nums:
    print("An element in this list is:", n)

# This kind of loop is called a 'for each' loop. Unlike the previous kind of loop, the
# variable `n` will take on the values of the elements in the list itself, not their indices.
# So on the first iteration, n=53, then n=38, and then n=49, and so on...
# This kind of loop is usually used when we only require the elements inside the list and NOT
# their positions in the list


#########################
# EXERCISE
#########################

# Write a Python program that will make a two separate lists of `names` and `ages` such that
# the first element in the `names` list will correspond to the first element in the `ages` list.
# Make sure both lists are of the same length. Then loop through and print:
#               "NAME is AGE years old"

# Note: Given the position in the `names` list, that person will have an age at the same position in the `ages` list.

