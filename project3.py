#Project 3
#CMSC 210
#Yvon Dushime

#importing the sys module
import sys
# read the input from the command
timesFar = int(sys.argv[1])
    #part 1 of the final scentence
    part_1 = "A long time ago in a galaxy "
    #part 2 of final scentence
    part_2 = "far "
    #part 3 of the final scentence
    part_3 = "away..."
    #printing the final result
    print(part_1 + part_2 * timesFar + part_3)
    
 #telling what the computer to do if the input is less than 1
 if timesFar < 1:
     print (" The Universe is vast your view is too small.")
#telling the computer what to do if the input is greater than 5
elif timesFar >5:
    print("Enough already: you're going too far.")
#telling the computer what to if the inoput is between 1 and 5 and making
elif 1<= tinesFar and timesFar <= 5:
    #calling the far funtion
    far()
 