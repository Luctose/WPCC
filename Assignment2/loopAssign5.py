"""
Lucas Sarweh
110042658
Date: 28 Dec 2020
"""

# Main function
def main():
    # Get input
    userString = input("Enter a string: ")

    # Make the square of words
    for i in range(len(userString) + 1):
        if i == 0:
            print(userString + userString[0])
        elif i == len(userString):
            print(userString[0] + userString[::-1])
        else:
            print(userString[len(userString) - i] + " " * (len(userString) - 1) + (userString[i]))

# Thingy
if __name__ == "__main__":
    main()