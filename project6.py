#Yvon Dushime
#CMSC 210
#Project 6
import sys

numRows = int(sys.argv[1])

if numRows < 0 :
    print("Invalid input value. The number of rows cannot less than 0.")
elif numRows > 20 :
    print("Invalid input value. The number of rows cannot be more than 20.")
else:
    total = 0
    #i equal to rows2
    for i in range(numRows):
    #j range equal to coloms
        for j in range (numRows):
    #each line added one ot continue pattern
            print("@ ",end="")
            total = total + 1
    #print til end
    print()
    print(total)

