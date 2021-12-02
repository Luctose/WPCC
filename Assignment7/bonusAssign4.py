"""
Lucas Sarweh
110042658
Date: 11 Jan 2021
"""

# Find a number in pascals triangle
def pascal(row, column):
    # State 1st in triangle
    if row == 1 or column == 1 or column == row:
        return 1
    
    return pascal(row - 1, column - 1) + pascal(row - 1, column)

# Main function
def main():
    print(pascal(0, 3))

# Thingy
if __name__ == "__main__":
    main()