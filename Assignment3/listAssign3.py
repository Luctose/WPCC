"""
Lucas Sarweh
110042658
Date: 30 Dec 2020
"""

import random

def main():
    # Define list holding birthdays
    birthdayList = []

    # While no duplicates
    while True:
        # Add random day of the year to list
        birthdayList.append(random.randint(1, 365))

        if len(birthdayList) != len(set(birthdayList)):
            break
    
    # Tell user how many birthdays were generated
    print("Birthdays generated before duplicate: %d" % len(set(birthdayList)))


if __name__ == "__main__":
    main()