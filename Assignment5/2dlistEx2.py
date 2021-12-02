# WPCC
# 2dlistEx2.py

# Say we have the following 10x10 2D list:

nums = [
        [74, 47, 82, 56, 17, 34, 84, 67, 37, 67],
        [10, 84, 95, 55, 5,  48, 25, 73, 35, 70],
        [10, 74, 94, 51, 29, 98, 6,  13, 27, 79],
        [44, 51, 54, 26, 36, 64, 23, 73, 39, 5 ],
        [45, 24, 83, 92, 94, 13, 93, 69, 86, 57],
        [51, 94, 78, 46, 60, 44, 5,  92, 29, 59],
        [32, 9,  75, 40, 41, 50, 5,  0,  63, 52],
        [65, 5,  55, 36, 11, 46, 74, 71, 67, 0 ],
        [46, 25, 31, 65, 27, 30, 83, 83, 30, 34],
        [82, 36, 50, 69, 83, 29, 27, 84, 27, 70]
    ]

# How would we visit every number?
# Well first we could loop through every list in `nums`,
# then loop through every element in those lists

# This is how it would look in Python code

for numberList in nums: # This loops through every single list
    for number in numberList: # This loops through every element inside of the outer for-loop's list
        print(number, end=' ')
    print('')
# The above uses the 'for each' loop to go through each element. Recall that we would usually use
# this kind of loop when we aren't concerned with the element's position, but just the values of the 
# elements themselves.

# More likely than not, we *will* be concerned where the element in located in said 2D list.
# So we can loop through our 2D list like this:

print('')
for row in range(len(nums)): # Loop through the indices of the lists
    for col in range(len(nums[row])): # Loop through the indices of the elements inside of that list
        print(nums[row][col], end=' ')
    print('')
# The difference here is that we have the `row` and `col` variables indicating the positions of each
# element in the 2D list


#########################
# EXERCISE
#########################

# Write a Python program that makes 2 functions. The first function will make a new 10x10 2D list
# containing floats (initialize all the elements to 0.0), and return the newly created list. The
# second function will take a 2D list as a parameter and print out every single *list* inside of
# the 2D list (not the elements themselves, just the lists as a whole).
# Then call the first function to make a new list, and pass the list into the second function to print
# it out

# The call should look like this:
'''
newList = make_new_list()
printList(newList)
'''


