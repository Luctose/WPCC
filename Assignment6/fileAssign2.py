"""
Lucas Sarweh
110042658
Date: 09 Jan 2021
"""

# Main function
def main():
    # Open the people file
    peopleFile = open("people.txt")
    people = peopleFile.read().split("\n")
    # Store 2dlist with each row containing info about one person
    peopleList = []
    for i in range(len(people)):
        peopleList.append(people[i].split(","))

    # Close file
    peopleFile.close()

    # Store unique hobbies
    hobbies = []
    # Find hobbies
    for row in range(len(peopleList)):
        for col in range(1, len(peopleList[row])):
            hobbies.append(peopleList[row][col])
    # Make the hobbies unique
    hobbies = list(set(hobbies))

    # Create file names based on hobbies set
    for i in range(len(hobbies)):
        newfile = open(hobbies[i] + ".txt", "x")
        # Loop through the 2d list of names and hobbies and if the filename = one of a persons hobbies add them to the file
        for row in range(len(peopleList)):
            for col in range(1, len(peopleList[row])):
                if peopleList[row][col] == hobbies[i]:
                    newfile.write(peopleList[row][0] + "\n")
                    break
        # Close the file
        newfile.close()


# Thingy
if __name__ == "__main__":
    main()