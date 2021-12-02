"""
Lucas Sarweh
110042658
Date: 03 Jan 2021
"""

# Determines if a number is prime
def isPrime(num):

    # True if prime false if not
    if num > 1:
        for i in range(2, int(num)):
            if num % i == 0:
                return False
    return True

# This will take lists inside of lists and make the list elements only numbers
def flattenList(array):
    
    if len(array) == 0:
        return array
    
    if isinstance(array[0], list):
        return flattenList(array[0]) + flattenList(array[1:])

    return array[:1] + flattenList(array[1:])

# This will give prime factors using recursion
def primeFactor(num):
    
    if (isPrime(num)):
        return int(num)
    else:
        for i in range(2, int(num)):
            if (num % i == 0 and isPrime(i)):
                return [primeFactor(num / i), primeFactor(i)]

# This will find LCM using prime factors
def lowestCommonMultiple(num1, num2):

    # If they are the same number
    if num1 == num2:
        return num1
    # If num1 or num2 arn't already prime numbers
    elif not isPrime(num1) and not isPrime(num2):
        # Get the prime factor lists of both parameters
        primeList1 = flattenList(primeFactor(num1))
        primeList2 = flattenList(primeFactor(num2))
    # If one is prime
    elif isPrime(num1) and not isPrime(num2):
        primeList1 = [num1]
        primeList2 = flattenList(primeFactor(num2))
    # Second case if one is prime
    elif not isPrime(num1) and isPrime(num2):
        primeList1 = flattenList(primeFactor(num1))
        primeList2 = [num2]
    else:
        # Return product if they are both primes and not the same number
        return num1 * num2
    
    # Combined list will store prime factors of both
    combinedList = primeList1 + primeList2
    # This will store duplicate numbers of both lists
    dupList = []
    # This will store offset for deletion of list elements
    offset = 0
    # Stores the product of combined factors which will be the result
    product = 1

    # First store the duplicate numbers in dupList
    for i in primeList1:
        if i in primeList1 and i in primeList2:
            dupList.append(primeList1[primeList1.index(i)])
        
    # Then take combined list subtract duplicate list
    for i in range(len(combinedList)):
        for j in range(len(dupList)):
            if combinedList[i - offset] == dupList[j - offset]:
                del combinedList[i]
                del dupList[j]
                offset += 1
        
    # Multiply the list of prime factors to find LCM
    for i in combinedList:
        product *= i
        
    return product



def main():

    print(lowestCommonMultiple(77, 300))

if __name__ == "__main__":
    main()