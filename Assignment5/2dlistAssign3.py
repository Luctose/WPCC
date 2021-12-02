"""
Lucas Sarweh
110042658
Date: 06 Jan 2021
"""

# Import needed libraries
import math
import random

# Calculate distance
def distance(x1, y1, x2, y2):
    # Return the distance
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Checks if trees are too close
def checkDist(checkList, newX, newY):
    
    # This list keeps track of tree location
    location = []

    # Store the locations of the current trees
    for i in range(len(checkList)):
        for j in range(len(checkList[i])):
            if checkList[i][j] == 1:
                location.append([i, j])

    # Check if the 1's are 3 meters apart (False for too close)
    for i in location:
        if distance(newX, newY, i[0], i[1]) <= 3:
            return False
    
    # If all good return True
    return True

# Randomly assigns a tree
def randomAssign(randolist):
    # Number of assigned trees
    trees = 0

    # Randomly generated coordinates (first one doesn't need a checker)
    x = random.randint(0, 29)
    y = random.randint(0, 29)

    # Place first tree
    randolist[x][y] = 1

    while (trees < 10):
        # Generate new coordinates
        x = random.randint(0, 29)
        y = random.randint(0, 29)

        # Check if these new coords are good with the rest of the trees
        if checkDist(randolist, x, y):
            randolist[x][y] = 1
            trees += 1
    
    # Return list
    return randolist

# Initializes the list to have underscores
def listInit(x, y):

    # Make an m by n list (2d) and return it
    return [[0 for i in range(y)] for j in range(x)]

# Main function
def main():
    # Create an empty 30 x 30 2d list
    backyard = randomAssign(listInit(30, 30))

    # Print result
    for i in range(len(backyard)):
        for j in range(len(backyard)):
            if backyard[i][j] == 1:
                print("X", end=" ")
            else:
                print("_", end=" ")
        print("")

# Thingy
if __name__ == "__main__":
    main()