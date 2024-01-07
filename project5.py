#Yvon Dushime
#Template File 
#   Using Math Functions

import math
import sys

x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])


#  Determine slope of a line through two points by calculations
#  Store the result in a Variable named slope
slope = (y2-y1)/(x2-x1)

#  Calculates the distance bewteen two points
#  Store the result in a variable named distance
distance = math.sqrt((x2-x1)^2 + (y2-y1)^2)

print("The slope of the line is", slope)
print("The distance bewteen the points is", distance)

