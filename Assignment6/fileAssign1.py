"""
Lucas Sarweh
110042658
Date: 09 Jan 2021
"""

# Remove unwanted puncuation from a string
def wordClean(stringList):
    for i in range(len(stringList)):
        stringList[i] = stringList[i].strip(" ,.?!;:[]&*()^%#@-_=+}{`~|\'\"\\\n").lower()
    return stringList

# Main function
def main():
    # Open the dictionary to read and use different file encoding to remove the weird characters ï»¿a
    dictFile = open("dictionary.txt", "r", encoding="utf-8-sig")
    # Seperate each word into list elements
    dictionary = wordClean(dictFile.read().split("\n"))
    # Close file stream
    dictFile.close()

    # Now open and read the story
    storyFile = open("story.txt", "r", encoding="utf-8-sig")
    # Seperate each word into list elements and remove punctuation
    story = wordClean(storyFile.read().split())
    # Close file stream
    storyFile.close()

    # New list to store words not in the dictionary
    notFound = []
    # bool that will determine wether a word is found in the dictionary
    found = False

    # Compare the two word lists
    for i in range(len(story)):
        # Skips any elements that were just punctuation and are empty lists from wordClean
        if len(story[i]) == 0:
            pass
        # If the current word doesn't start with "z"
        elif story[i][0] != "z":
            # Because dictionary.txt is so large use asciicode to only loop the sections that the current word starts with
            for j in range(dictionary.index(story[i][0]), dictionary.index(chr(ord(story[i][0]) + 1))):
                # if the word is in the dictionary break and move on to the next letter
                if story[i] == dictionary[j]:
                    found = True
                    break
            # If it was not found append it to the not found list
            if found == False:
                notFound.append(story[i])
            else:
                found = False
        else: # If the word starts with "z" the range will be different because it's asciicode + 1 is not a letter
            # Because dictionary.txt is so large use asciicode to only loop the sections that the current word starts with
            for j in range(dictionary.index("z"), len(dictionary)):
                # if the word is in the dictionary break and move on to the next letter
                if story[i] == dictionary[j]:
                    found = True
                    break
            # If it was not found append it to the not found list
            if found == False:
                notFound.append(story[i])
            else:
                found = False
    
    # Print the words not found in the dictionary
    print(notFound)

# Thingy
if __name__ == "__main__":
    main()