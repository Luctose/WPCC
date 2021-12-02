"""
Lucas Sarweh
110042658
Date: 23 Dec 2020
"""

# Main function
def main():
    # Get the coordinates of the two points from the user
    x1 = int(input("Enter two points on a line:\nx1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))

    # Calculate the m and b values of y = mx + b
    m = (y2 - y1)/(x2 - x1)
    b = y1 - m*x1

    # Get coords of test point
    j = int(input("Enter a test point:\nj: "))
    k = int(input("k: "))

    # Test if the inputted x value gives the inputted y value
    if m*j + b == k:
        print("The point (%d, %d) is on the line y = %.3f * x + %.3f" % (j, k, m, b))
    else:
        print("The point (%d, %d) is NOT on the line y = %.3f * x + %.3f" % (j, k, m, b))

# Thingy
if __name__ == "__main__":
    main()