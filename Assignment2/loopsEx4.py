# WPCC
# loopsEx4.py

# Until now, we have discussed 2 different kinds of `for` loops:
# a for loop that loops through a range of numbers, and
# a for loops through the letters of a string.

# The while loop:
# 'for loops' are great for some problems, but sometimes you don't
# know how many iterations you need to do, you do don't know the range
# in which to loop. A while loop on the other hand behaves quite similar
# to common English. If I say:
#	while your tea is too hot, add a chip of ice.

# Presumably you would test your tea. If it were too hot,
# you would add a little ice. Upon testing again, if it were too
# hot, you would add a little ice again, and again until your
# condition (your tea is too hot) is false, at which point
# you will cease adding a chip of ice.

# The syntax of a while loop is as follows:
# 	while condition:
# 		do something


some_number = 115
while some_number > 112:
	print(some_number)
	some_number = some_number - 1

# In the example above, the condition is tmp > 112.
# Inside the loop tmp is printed out and then
# the value of tmp is decreased by 1 until the condition
# is false.

# Remark: The above example could be replaced by a `for`
# loop because we know exactly how many times to iterate

# Be careful when constructing `while` loops: if the
# condition is always true, the loop will run forever:
# For example, if I made a loop like this:
"""
while 1 == 1:
    print("Whee!")
"""
# the condition is ALWAYS true, so the while loop will run indefinitely

# Let's use a while loop to ask the user for data:

while True:
	condition = input("Infinite loop enter d to exit: ")
	if condition == 'd':
		break

# Since the condition will always be true (because it IS True!)
# the following loop will be infinite. Then how does this program
# end? By using the `break` keyword. If Python comes across the `break`
# keyword, the loop will be forced to end. So in the example above,
# the user is asked for input an infinite number of times until they
# input 'd', upon which the program will "break" out of the loop.

# Example 3
# Consider this code, a slight variation made to the first example:
# run the program and careful follow what is outputted.

tmp = 115
while tmp > 112:
	tmp = tmp - 1
	print(tmp)


# In this example, 115 is not printed, but 112 is.
# However your condition stated tmp > 112, not 
# tmp >= 112. What's happening here is tmp is printed
# after its value has been decremented. The loop will only
# check the condition once the loop iterates fully.
# Even though the value is 112 the loop, it has to execute
# the print statement and then go back to the start
# to check the condition.

#########################
# EXERCISE
#########################

# Run a python program that generates random numbers from 1 to 100
# (inclusive) until the number 49 is generated. Then print how many
# numbers where generated before 49 was.

print("")
import random

