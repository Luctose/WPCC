"""
Lucas Sarweh
110042658
Date: 30 Dec 2020
"""

def main():
    # Define list to store marks
    markList = []

    # Loop until user exits
    while True:
        # Get user input
        userInput = int(input("Please enter a mark: "))
        # If they want to exit
        if userInput == -1:
            break
        # Store mark into list
        markList.append(userInput)
    
    # Sort the list
    markList.sort()

    # If there are 6 or more marks entered
    if len(markList) >= 6:
        # New list to store top marks
        bestMarks = []
        # Store top 6 into bestMarks
        for i in range(6):
            bestMarks.append(markList[len(markList) - i - 1])
    else:
        # Just set the best marks to the original list
        bestMarks = markList[::-1]
    
    # Find average
    avg = 0
    for j in bestMarks:
        avg += j
    avg = avg / len(bestMarks)
    
    # Find median
    med = 0
    size = len(bestMarks)
    
    # Finding median is different depending on the size of the array
    if size % 2 == 0:
        med = (bestMarks[(size - 1) // 2] + bestMarks[(size) // 2]) / 2
    else:
        med = bestMarks[(size) // 2]

    # Print results
    print("Average of top 6: %f\nMedian of top 6: %f" % (avg, med))

if __name__ == "__main__":
    main()