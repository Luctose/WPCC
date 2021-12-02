"""
Lucas Sarweh
110042658
Date: 22 Dec 2020
"""

# Main function
def main():
    # Get user input for temperature in celcius
    userInput = float(input("Please enter a temperature in celcius: "))

    # Convert to celcius and print to console
    print("%.2f F" % (userInput * (9/5) + 32))

# Thing that you do for some reason
if __name__ == "__main__":
    main()