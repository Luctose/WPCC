# WPCC
# listEx2.py

# We know how to make lists, but how can we use them
# in a useful way?

# Let's make a short program that will ask the user
# for a bunch of names and add them into a list:

names = []
while True:
    user_input = input("Please enter a name (x to exit): ")
    if user_input == 'x':
        break
    names.append(user_input)

print(names)

# Names will store an arbitrary amount of data. The user can keep
# typing in names to their heart's desire, and our program will be able
# to keep track of it

# Now how can we manipulate this data?
# Like we saw in the previous section, we can index a string
# or even get a subsection of a string using the [] notation.
# The same thing applies to lists:

places = ['Toronto', 'Chicago', 'Windsor', 'Detroit', 'Edmonton']
print(places[0])

# The above print statement will print only the first element of `places`.
# All the things we learned about string indexing will apply to lists:

print(places[1:2])  # Print the sub list from index 1(inclusive) to 2(exclusive): ['Chicago']
print(places[::2])  # Print the list containing every other item in `places`,
                    # starting from index 0 until the end of the list

# Note: if the first index is not specified, it's assumed to be 0.
# Note: if the last index is not specified, it's assumed to be the end of the list.


# I've decided that I only want Canadian cities in my list of places.
# How do we remove items from our list?

# We can remove an item if we know its index. Say we want to remove the item
# that sits at index 1:
print("")

print(places)
del places[1]

print(places)

# Observing the output of the prints, we can see that 'Chicago' has been removed.
# Now I want to remove 'Detroit' from the list. We can remove an item
# by specifying its value:

places.remove('Detroit')
print(places)

# The `remove` function will act on the list `places`, searching for 'Detroit'
# and removing it

#########################
# EXERCISE
#########################

# Write a Python program that makes a list of famous cities.
# Then ask the user what cities they have already been until
# they enter 'x'. Check if the cities are in the list,
# then remove it if it is.

cities = ["Bangkok", "London", "Paris", "Dubai", "Singapore", "New York", "Kuala Lumpur", "Tokyo", "Istanbul" "Seoul", "Antalya", "Phuket", "Mecca", "Hong Kong", "Mila", "Palma de Mallorca", "Barcelona", "Pattaya", "Osaka", "Bali"]

