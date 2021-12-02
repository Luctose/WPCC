"""
Lucas Sarweh
110042658
Date: 03 Jan 2021
"""

# This function determines if a word is a palidrome
def palindrome(word):
    if word[::] == word[::-1]:
        return True
    else:
        return False

# Main function
def main():
    # Example function calls
    print(palindrome("racecar"))
    print(palindrome("python"))
    print(palindrome("madam"))

# Thingy
if __name__ == "__main__":
    main()