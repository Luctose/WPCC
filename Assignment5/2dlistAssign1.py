"""
Lucas Sarweh
110042658
Date: 05 Jan 2021
"""

# Determine if a 2d list is empty or not
def empty(tdlist):
    # Loop through each number in list and search for non zeroes
    for lists in tdlist:
        for num in lists:
            if num != 0:
                # If we find a non zero return false
                return False
    
    # If no non zeroes were found return True
    return True

# Find the coordinates of a value in a 2d list
def find(tdlist, key):
    # Loop through each number to find key
    for row in range(len(tdlist)):
        for col in range(len(tdlist[row])):
            # If we find the key in the list
            if tdlist[row][col] == key:
                # Return the current position
                return [row, col]
    
    # If not found return [-1, -1]
    return [-1, -1]

# Main function
def main():
    print(empty([[0, 0], [0, 0, 0, 0, 0], [0, 0, 1]]))
    print(find([[78, 45, 33], [44, 22, 1, 2], [9, 0, 4]], 2))

# Thingy
if __name__ == "__main__":
    main()