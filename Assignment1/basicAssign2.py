"""
Lucas Sarweh
110042658
Date: 23 Dec 2020
"""

# Main function
def main():
    # Ask user for input
    userInput = int(input("Please enter your grade: "))

    # Work out what letter grade is equivalent
    if userInput >= 80:
        print("Your grade is A!")
    elif userInput >= 70:
        print("Your grade is B!")
    elif userInput >= 60:
        print("Your grade is C.")
    elif userInput >= 50:
        print("Your grade is D.")
    else:
        print("Your grade is F.")

# Thingy
if __name__ == "__main__":
    main()