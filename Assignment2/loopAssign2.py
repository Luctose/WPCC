"""
Lucas Sarweh
110042658
Date: 27 Dec 2020
"""

# Main function
def main():
    # Ask for number
    num = int(input("Please enter an integer: "))

    # Init sum
    sum = 0

    # sum series
    for i in range(num):
        sum += (1 / (i + 1))
    
    # Print result
    print(sum)

# Thingy
if __name__ == "__main__":
    main()