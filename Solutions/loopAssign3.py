# WPCC
# loopAssign3.py

userinput = input("Enter a string: ")

# Best solution

# Split by spaces
s = userinput.split(' ')
for i in s:
    # The the list will contain empty strings if there was more than 2 spaces
    if i != '':
        print(i, end=' ')

print()

# Another solution
# Keep track of how many spaces went by
space_count = 0
sol = ""
for i in range(len(userinput)):
    # update space_count if there's a space
    if userinput[i] == ' ':
        space_count += 1
    else:
        space_count = 0

    # add to sol if there's only been 1 space or less
    if space_count <= 1:
        sol += userinput[i]

print(sol)
