# WPCC
# loopAssign5.py

userinput = input("input: ")

print()
# The first line of the square: the whole word + first letter of the word
print(userinput + userinput[0])
for i in range(1, len(userinput)):
    # The left column
    s = userinput[len(userinput)-i]

    # The spaces in the middle
    s += ' '*(len(userinput)-1)

    # The right column
    s += userinput[i]
    print(s)

# The last line of the square: the first letter + the word backwards
print(userinput[0] + userinput[::-1])

