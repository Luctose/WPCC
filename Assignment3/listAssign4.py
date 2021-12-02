"""
Lucas Sarweh
110042658
Date: 30 Dec 2020
"""

import random

def main():
    # Define a list of names
    nameList = []

    # Get names until user enters x
    while True:
        # Get names
        name = input("Enter name (x to generate assignments): ")
        # Check if it is x
        if name == "x":
            break
        # Append name to list
        nameList.append(name)
    
    # Duplicate the list
    newList = nameList[:]
    random.shuffle(nameList)

    # Create variable to check if done
    done = True

    while done:
        # Randomize the list
        random.shuffle(newList)
        done = False

        # Make sure people don't buy for themselves
        for i in range(len(newList)):
            if newList[i] == nameList[i]:
                done = True
    
    # Output the assignments
    for j in range(len(newList)):
        print("%s gifts %s" % (nameList[j], newList[j]))

if __name__ == "__main__":
    main()