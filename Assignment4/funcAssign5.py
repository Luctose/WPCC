"""
Lucas Sarweh
110042658
Date: 03 Jan 2021
"""

# Recursive palindrome
def rPalindrome(word):
    # If there is only one letter left or no letters left
    if len(word) == 1 or len(word) == 0:
        return True
    # If outside letters of current word are the same
    elif word[0] == word[len(word) - 1]:
        # Remove outside letters and do it again
        return rPalindrome(word[1:len(word) - 1])
    else:
        # If not return false
        return False

# Main function
def main():
    print(rPalindrome("racecar"))
    print(rPalindrome("python"))
    print(rPalindrome("madam"))

# Thingy
if __name__ == "__main__":
    main()