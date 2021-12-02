"""
Lucas Sarweh
110042658
Date: 11 Jan 2021
"""

import random

# Global
exclude = []

# Generates a random question and answer
def randomQ():
    # World cup winners
    winnerList = [["Uruguay", 1930], ["Italy", 1934], ["Italy", 1938], ["Uruguay", 1950], ["West Germany", 1954], ["Brazil", 1958], ["Brazil", 1962],
    ["England", 1966], ["Brazil", 1970], ["West Germany", 1974], ["Argentina", 1978], ["Italy", 1982], ["Argentina", 1986],
    ["West Germany", 1990], ["Brazil", 1994], ["France", 1998], ["Brazil", 2002], ["Italy", 2006], ["Spain", 2010], ["Germany", 2014],
    ["France", 2018]]

    # First generate the answer
    question = []
    Good = True

    if len(exclude) > 0:
        while(True):
            Good = True
            temp = random.randint(0, 20)
            for k in range(len(exclude)):
                if winnerList[temp][0] == winnerList[exclude[k]][0]:
                    Good = False
            if Good == True:
                question.append(temp)
                break
    else:
        question.append(random.randint(0, 20))
    
    # Add already used answer to questions to exclude
    exclude.append(question[0])

    # Then generate the wrong answers
    for _ in range(3):
        while(True):
            Good = True
            temp = random.randint(0, 20)
            for j in range(len(question)):
                if winnerList[temp][0] == winnerList[question[j]][0]:
                    Good = False
            if Good == True:
                question.append(temp)
                break
    
    # Return randomized question list
    return [winnerList[question[0]], winnerList[question[1]], winnerList[question[2]], winnerList[question[3]]]

# Print the multiple choice question
def multipleChoice(questions):
    # List keeps track of 0-3 for questions
    numList = [0, 1, 2, 3]
    random.shuffle(numList)

    while(len(numList)):

        # Print the multiple choice questions
        print("Which team won in the year %d" % questions[0][1])
        print("1. %s\n2. %s\n3. %s\n4. %s" % (questions[numList[0]][0], questions[numList[1]][0], questions[numList[2]][0], questions[numList[3]][0]))
        answer = int(input("Enter your choice: "))

        # Check if they are correct
        if questions[numList[answer - 1]][1] == questions[0][1]:
            print("Correct!")
            return True
        else:
            print("Incorrect! The answer was %s" % questions[0][0])
            return False


# Main function
def main():
    # Init values
    correct = 0
    
    for _ in range(8):
        if multipleChoice(randomQ()):
            correct += 1
    
    if correct / 8 >= 0.8:
        print("You got %.1f%%! Excellent!" % (correct * 100/ 8))
    elif correct / 8 >= 0.6:
        print("You got %.1f%%. Pretty good!" % (correct * 100/ 8))
    elif correct / 8 >= 0.5:
        print("You barely passed. You got %.1f%%." % (correct * 100/ 8))
    elif correct / 8 >= 0.3:
        print("Sorry you failed. You got %.1f%%." % (correct * 100/ 8))
    else:
        print("Wow! Guessing ain't your strong suit. You got %.1f%%..." % (correct * 100/ 8))
    


# Thingy
if __name__ == "__main__":
    main()