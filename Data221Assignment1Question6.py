#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 Question 6 Data 221
def distributionAnalysis(values):
    #reject empty list
    if len(values) == 0:
        return "The list cannot be empty."

    #reject non numeric items
    for item in values:
        if not isinstance(item, (int, float)):
            return "All values in the list must be numbers."

    #total count for percentages
    elementCount = len(values)

    #unique sorted keys for the distribution
    sortedKeys = sorted(set(values))

    #store final mapping here
    distributionMap = {}

    #go through each key and count how many are <= it
    for currentKey in sortedKeys:
        runningCount = 0
        for candidate in values:
            if candidate <= currentKey:
                runningCount += 1

        #convert count to percent
        percentUpToKey = (runningCount / elementCount) * 100
        distributionMap[currentKey] = percentUpToKey

    return distributionMap


#main program
#read raw user input
rawLine = input("Enter a list of numbers separated by spaces: ")

#split into pieces
textParts = rawLine.split()

#build numeric list
numberValues = []
inputOk = True

for text in textParts:
    try:
        numberValues.append(float(text))
    except:
        print("All values must be numbers.")
        inputOk = False
        break

#run if valid and not empty
if inputOk and len(numberValues) > 0:
    output = distributionAnalysis(numberValues)
    print("Distribution Dictionary:")
    print(output)
elif inputOk and len(numberValues) == 0:
    print("The list cannot be empty.")