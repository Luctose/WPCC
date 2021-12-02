"""
Lucas Sarweh
110042658
Date: 11 Jan 2021
"""

# Tests if a point exists on a quadratic
def quadratic(a, b, c, x, y):
    # Test if it is on the line
    if a*(x**2) + b*x + c == y:
        return True
    return False

def main():
    # Get user input
    a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))
    x, y = float(input("x = ")), float(input("y = "))
    # Call function
    print(quadratic(a, b, c, x, y))

# Thingy
if __name__ == "__main__":
    main()