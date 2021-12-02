"""
Lucas Sarweh
110042658
Date: 11 Jan 2021
"""

# Determines if the product code is valid
def isValid(code):
    # Split the first two parts of the product code
    code = code.split(" ")

    # Number of digits
    digits = 0
    product = 1
    temp = 0

    # Check the all letters are capital
    for letter in code[0]:
        if letter.isupper() or letter.isnumeric():
            if letter.isnumeric():
                digits += 1
                if digits % 2 == 0:
                    temp = (temp * 10) + int(letter)
                    product *= temp
                    temp = 0
                else:
                    temp = int(letter)
        else:
            return False
            
    # Return stuff
    if digits == 6 and product == int(code[1]):
        return True
    
    return False

# Main function
def main():
    print(isValid(input("Enter a product code: ")))

if __name__ == "__main__":
    main()