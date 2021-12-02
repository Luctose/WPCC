"""
Lucas Sarweh
110042658
Date: 30 Dec 2020
"""

def main():
    # Define a list that stores data about the calendar
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Sum of days
    summ = 0

    # Ask for day and month
    month = int(input("Month: "))
    day = int(input("Day: "))

    # Check for invalid months
    if month > 12 or month <= 0:
        print("That month does not exist.")
        return 0
    
    # Check for invalid days
    if day > year[month - 1] or day < 1:
        print("That day does not exist in the current month.")
        return 0

    # Calculate how many days have passed in the year
    for i in range(month - 1):
        summ += year[i]

    # Add the current unfinished month
    summ += day

    # Print result
    print("That's day %d of the year" % summ)

if __name__ == "__main__":
    main()