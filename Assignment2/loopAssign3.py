"""
Lucas Sarweh
110042658
Date: 27 Dec 2020
"""

# Main function
def main():
    # Get user input
    userString = input("Enter a string: ")
    numList = []

    # Remove extra spaces (This is very interesting code idk how to do it properly, but it does work)
    for i in range(len(userString) - 1):
        if(userString[i] == " " and userString[i + 1] == " "):
            numList.append(i + 1)
    nope = True
    for n in range(len(userString)):
        for j in numList:
            if n == j:
                nope = False
        if nope == True:
            print(userString[n], end='')
        nope = True


# Thingy
if __name__ == "__main__":
    main()