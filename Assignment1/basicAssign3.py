"""
Lucas Sarweh
110042658
Date: 23 Dec 2020
"""

# Import libraries
import random

# Main function
def main():
    # Ask user for guess
    guess = int(input("Enter a guess between 1 and 9: "))

    # Randomize a number
    answer = random.randint(1, 9)

    # Check if guess is equal to random number
    if(guess == answer):
        print("Correct! The number was %d." % answer)
    else:
        print("Incorrect. The number was %d" % answer)

# Thingy
if __name__ == "__main__":
    main()