# WPCC
# loopAssign1.py

userinput = input("Enter a string: ")

rev = ""
# Loop from end of string until 0, going by (-1) each time
for i in range(len(userinput)-1, -1, -1):
    rev += userinput[i]
print(rev)





# An alternative solution
rev = userinput[::-1]
print(rev)

