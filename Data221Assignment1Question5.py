#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 question 5 Data 221
import math

def circleAreaCoverage(firstRadius, secondRadius):
    #validate integer inputs
    if not isinstance(firstRadius, int) or not isinstance(secondRadius, int):
        return "Both radii must be positive integers."

    #validate positivity
    if firstRadius <= 0 or secondRadius <= 0:
        return "Both radii must be positive integers."

    #compute areas
    firstArea = math.pi * (firstRadius ** 2)
    secondArea = math.pi * (secondRadius ** 2)

    #pick bigger/smaller without min/max
    if firstArea >= secondArea:
        bigArea = firstArea
        smallArea = secondArea
    else:
        bigArea = secondArea
        smallArea = firstArea

    #compute percent coverage
    coveragePercent = (smallArea / bigArea) * 100
    return coveragePercent


#main program
#grab raw inputs
rawFirst = input("Enter the radius of the first circle: ")
rawSecond = input("Enter the radius of the second circle: ")

#check digit strings first
if (not rawFirst.isdigit()) or (not rawSecond.isdigit()):
    print("Both radii must be positive integers.")
else:
    #convert to ints
    firstRadius = int(rawFirst)
    secondRadius = int(rawSecond)

    #run and print
    answer = circleAreaCoverage(firstRadius, secondRadius)
    print("Percentage of coverage:", answer, "%")