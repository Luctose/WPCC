"""
Lucas Sarweh
110042658
Date: 03 Jan 2021
"""

# Returns the difference between two lists
def subtract(list1, list2):
    # Catch if both same
    if list1 == list2:
        return []

    # Copy first list
    newList = list1[:]
    # Offset to avoid list index error
    offset = 0

    # Delete element if found in both lists
    for i in range(len(list2)):
        for j in range(len(newList)):
            if newList[j - offset] == list2[i]:
                del newList[j - offset]
                offset += 1

    # Return result
    return newList

# Main function
def main():
    # Function call example and print
    print(subtract([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 4, 5, 6, 7, 8]))

# Thingy
if __name__ == "__main__":
    main()