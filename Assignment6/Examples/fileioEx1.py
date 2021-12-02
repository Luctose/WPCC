# WPCC
# fileioEx1.py

# One important reason people use Python is how easy it is to
# read/write and parse data in the form of a file.

# In Python, we can read a text file located on disk and use
# that information in our programs

# I've made a txt file so we can take a look at how we can read and write
# to it with Python

theTextFile = open('inFile.txt', 'r')

# The `open` command allows us to open a file that's located in *the same folder*
# as the python source file. So make sure that `inFile.txt` is in the same folder
# as `fileioEx1.py`

# The first argument of the `open` function is the file to open, and the second
# option is the mode we want to open the file in. Here are the different modes:
# - 'r': open for reading 
# - 'w': open for writing, truncating the file first. This will *wipe* the file, all data in the file will be deleted
# - 'x': create a new file and open it for writing
# - 'a': open for writing, appending to the end of the file if it exists

# We opened `inFile.txt` in read mode, meaning we can see the contents of the file without making changes to it.
# There are different functions we can use to read the contents of the file
# - read()      Will read the whole file as one big string. It will contain every byte of the file, including newlines
# - readlines() Will read the whole file as a list, where each element in the list is a line in the file (including newlines)
# - readline()  Will read only *one* line. Repeating calls will then get the second line, then the third ... etc.

# Note: when calling these read commands, the file's "cursor" will move to the end of the file (or to the next line for readline()).

# Let's see the contents of this file:
print('---------------------')
print('START OF READ COMMAND')
print('---------------------')
print(theTextFile.read())

theTextFile.seek(0) # to move the file's cursor back to the beginning of the file

print('---------------------')
print('START OF READLINES COMMAND')
print('---------------------')
print(theTextFile.readlines())

theTextFile.seek(0)

print('---------------------')
print('START OF READLINE COMMAND')
print('---------------------')
print(theTextFile.readline(), end='')
print(theTextFile.readline(), end='') # Just reads the first 2 lines of the file
print('---------------------')

# As we can see with these prints, the first read will print the whole file
# The second read command will read the whole file, but in a list (for easy iteration)
# The last two reads only read one line at a time (as strings)

# Once we are done opening a file, it's good practice to close it as well.
# This is especially important when *writing* to files. If a file is not closed,
# there's chance that Python will not actually write the data to the file.
# The reason is because Python uses buffered writing, but that's not in the scope
# of this camp.

# Here's how we can close "inFile.txt"
theTextFile.close()

