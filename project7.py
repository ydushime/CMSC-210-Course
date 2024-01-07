#Cmsc 210
# file name = "jabberwocky.txt"

def countLines(fileName):
    try:
        with open(fileName, 'r') as file:
            counter = 0
            for line in file:
                # strip the line of whitespace and check if it contains any alphanumeric characters
                if line.strip() and any(char.isalnum() for char in line):
                    counter += 1
            return counter
    except FileNotFoundError:
        return "File cannot be opened: " + fileName

def getLongestLine(fileName):
    try:
        with open(fileName, 'r') as file:
            longestLine = ''
            for line in file:
                # strip the line of whitespace and check if it contains any alphanumeric characters
                if line.strip() and any(char.isalnum() for char in line):
                    # compare the length of the current line to the length of the longest line so far
                    if len(line) > len(longestLine):
                        longestLine = line
            return longestLine.strip()
    except FileNotFoundError:
        return "File cannot be opened: " + fileName
    
