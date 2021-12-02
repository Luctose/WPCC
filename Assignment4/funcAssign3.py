"""
Lucas Sarweh
110042658
Date: 03 Jan 2021
I originally tried to make this recursive
using prime factors but it was a mess and
a way bigger file
"""

# Return the lowest common multiple
def lowestCommonMultiple(num1, num2):
    # Find greater number
    big = max(num1, num2)

    # Loop until both numbers are divisible
    while(True):
        if big % num1 == 0 and big % num2 == 0:
            break
        big += 1
    
    return big

# Main function
def main():
    print(lowestCommonMultiple(1033229799, 3932545545))

# Thingy
if __name__ == "__main__":
    main()