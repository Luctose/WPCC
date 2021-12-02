# WPCC
# loopAssign2.py

userinput = input("Enter a number: ")
n = int(userinput)

s = 0
for i in range(1, n+1):
    s += 1/i

print(s)

