"""
Lucas Sarweh
110042658
Date: 28 Dec 2020
"""
# For int min and max
import sys

# Main function
def main():
    # Define variables
    summ = 0
    numberOfInputs = 0
    userInput = 1
    maxx = -sys.maxsize
    minn = sys.maxsize

    # Loop user input until 0
    while userInput:
        # Get input
        userInput = int(input("Enter a number: "))
        # If 0 is not inputted
        if userInput:
            summ += userInput
            numberOfInputs += 1
            # If new min
            if userInput < minn:
                minn = userInput
            # If new max
            if userInput > maxx:
                maxx = userInput
    
    # Print results
    print("Average: %.1f\nLargest: %d\nSmallest: %d" % (summ / numberOfInputs, maxx, minn))

# Thingy
if __name__ == "__main__":
    main()