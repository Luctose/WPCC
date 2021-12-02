# WPCC
# loopsEx3.py

# We took a look at using for loops with the range function.
# But `range` isn't the only thing a `for` loop can iterate over.

some_word = 'word'
for letter in some_word:
    print(letter)

# In this for loop, the variable `letter` will take on the values of
# every character in the string `some_word`. This kind of for loop
# will give us every letter of the string, but we don't have the index
# value. This kind of "for" loop is best when the index is not needed,
# but only the values of each character.

# For example, if we wanted to print every letter of the alphabet, we could
# define a single string that contains every letter, then print all the
# letters separately

print("")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    print(letter)

#########################
# EXERCISE
#########################

# Write a Python program that makes a variable of value: '194629'
# Then loop through every digit, add 1 to it, and print it out. If the
# resulting digit is 10 or over, make it a zero.
# Remember that we can't add strings with integers

num = '194629'
