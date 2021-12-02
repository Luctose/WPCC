# WPCC
# basicEx6.py

# So far we've made our own variables that store
# data that we have defined. Let's look at how we can
# ask the user to enter in data that we can manipulate
# in our program

# We will use the `input` function to ask the user to enter
# some data

user_input = input("Please enter a number: ")

# We must give the input function a string. This string will be displayed
# to the user and wait for the to enter data. Once the user has entered
# the data, the `user_input` variable will take on that value

print(user_input)

# This will print exactly what the user entered. If we print its type:

print(type(user_input))
# We see that it's type is <class 'str'> i.e. a string

# That might be a problem if we want to ask the user for a number:

user_input = input("Please enter your age: ")

"""
print(user_input + 1)
"""
# What happens if we try to add 1 to the user's input?
# We will get an error because Python doesn't know how to add the
# string data type with the integer data type. But we know that `user_input`
# is in fact an integer number. So how can we tell Python that `user_input`
# is an integer?

# We must do something called "type casting." When we cast a variable to a
# different type, we're telling Python to interpret said variable as a
# different type.
# For example, we can cast `user_input` (which is a string) to an integer,
# that way we can do arithmetic operations on it:

x = int(user_input)

# Now `x` will hold the integer interpretation of `user_input` and we may now
# add 1 to it:

print(x + 1)


# We can cast variables to more types:
a = str(user_input)
b = float(user_input)
c = int(user_input)
b = bool(user_input)


#########################
# EXERCISE
#########################

# Write a program that asks the user to enter their birth month,
# birth day, and birth year into separate variables.
# Then output the sum of all three values.



