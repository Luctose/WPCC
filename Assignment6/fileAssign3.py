"""
Lucas Sarweh
110042658
Date: 09 Jan 2021
"""

# This function gives the rank for the given team
def teamRank(team, array):
    for k in range(len(array)):
        if team == array[k][0]:
            return array[k][1]
    # If not found
    return -1

# This function outputs True or False depending on whether the conditions
# of a fixed game are met
def isFixed(rank1, rank2, score1, score2, bet1, bet2):
    if (rank1 - rank2) > 10 or (rank2 - rank1) > 10:
        if rank1 > rank2:
            if score1 > score2:
                if bet1 / (bet1 + bet2) > 0.8:
                    return True

        elif rank2 > rank1:
            if score2 > score1:
                if bet2 / (bet1 + bet2) > 0.8:
                    return True
    # If all else fails
    return False

# Main function
def main():
    # Extract ranks.txt
    rankFile = open("ranks.txt")
    ranks = []
    for i in range(30):
        # Make 2d list containing Team and rank
        ranks.append([rankFile.readline().strip("\n"), i + 1])
    # Close file stream
    rankFile.close()

    # Extract matches.txt
    matchFile = open("matches.txt")
    match = matchFile.read().split("\n")
    matchList = []
    for i in range(len(match) - 1): # My 'matches.txt' had an extra line so it would append an empty list which would cause an error
        matchList.append(match[i].split(","))
    
    # Fixed match list
    fixedMatches = []

    # Find out which matches are fixed
    for row in range(len(matchList)):
        if isFixed(teamRank(matchList[row][0], ranks), teamRank(matchList[row][3], ranks),
        int(matchList[row][1]), int(matchList[row][4]), int(matchList[row][2]), int(matchList[row][5])):
            fixedMatches.append(matchList[row])
    
    # Print result
    print("FIXED MATCHES:")
    print("Underdog Rank Score Bets vs Favourite Rank Score Bets") # String formatting wasn't working for some reason so it is not lined up
    for i in range(len(fixedMatches)):
        if teamRank(fixedMatches[i][0], ranks) > teamRank(fixedMatches[i][3], ranks):
            print(fixedMatches[i][0], teamRank(fixedMatches[i][0], ranks), fixedMatches[i][1],
            fixedMatches[i][2], fixedMatches[i][3], teamRank(fixedMatches[i][3], ranks), fixedMatches[i][4], fixedMatches[i][5])
        else:
            print(fixedMatches[i][3], teamRank(fixedMatches[i][3], ranks), fixedMatches[i][4],
            fixedMatches[i][5], fixedMatches[i][0], teamRank(fixedMatches[i][0], ranks), fixedMatches[i][1], fixedMatches[i][2])

# Thingy
if __name__ == "__main__":
    main()