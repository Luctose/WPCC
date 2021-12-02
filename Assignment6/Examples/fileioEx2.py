# WPCC
# fileioEx2.py

# Let's look at how to write data to a file:

anotherTextFile = open('data.txt', 'w')

# We will open "data.txt" for writting this time

# Say we have a list of names we'd like to save:
names = ["Pappa\n", "Henry\n", "Jacob\n", "Hannah\n"]
# I've added new line characters ("\n") to the end of each name
# so that when we write the names to the file, each name will be on
# a new line

# We can use the `write()` function to write data to the file:
for name in names:
    anotherTextFile.write(name)

# When we loop through every name, the new line character at the end of
# each name will cause the names to be on different lines.

# Since we made a list of names, we can also use the `writelines()` function:
anotherTextFile.writelines(names)
# This function will take in a list and write all the elements into the file.

# Now this new txt file will contain every name twice since we wrote them twice:
# once with `write()`, once with `writelines()`

# We need make sure we close the file when we are done with it so that Python
# will successfully write it
anotherTextFile.close()

