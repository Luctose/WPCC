"""
Lucas Sarweh
110042658
Date: 23 Dec 2020
"""

# Main function
def main():
    # Define sum
    sum = 0

    # Get input from user
    userInput = int(input("Please enter a 3 digit number: "))
    
    # Loop through each digit
    for _ in range(3):
        sum += userInput % 10 # Add last digit to sum
        userInput = userInput // 10 # Floor 10 to remove last digit
    
    # Print summation result
    print(sum)

# Thingy
if __name__ == "__main__":
    main()