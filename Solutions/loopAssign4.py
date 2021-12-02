# WPCC
# loopAssign4.py

# Max and min
ma = -(2**32)
mi = 2**32

tot = 0
n = 0
while True:
    userinput = int(input("Enter a number: "))
    # Don't count 0, break immediately
    if userinput == 0: break
    n += 1
    tot += userinput

    ma = max(ma, userinput)
    mi = min(mi, userinput)

# Compute the average
average = tot/n

print("Average:", average)
print("Max:", ma)
print("Min:", mi)

