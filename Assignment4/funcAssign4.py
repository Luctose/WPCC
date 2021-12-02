"""
Lucas Sarweh
110042658
Date: 03 Jan 2021
"""

# Returns ith term in fibonacci sequence
def fib(i):
    # When we reach 0th term
    if i == 0:
        return 0
    # When we reach the 1st term
    elif i == 1:
        return 1
    # Any other term
    elif i > 1:
        return fib(i - 1) + fib(i - 2)

# Main function
def main():
    print(fib(10))
    
# Thingy
if __name__ == "__main__":
    main()