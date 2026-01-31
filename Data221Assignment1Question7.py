#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 Question 7 Data 221
def timeConversion(totalSeconds):
    #reject non int
    if not isinstance(totalSeconds, int):
        return "Input must be a non-negative integer."

    #reject negative
    if totalSeconds < 0:
        return "Input must be a non-negative integer."

    #wrap into a single day
    daySeconds = 24 * 60 * 60
    totalSeconds = totalSeconds % daySeconds

    #pull out hours first
    hour24 = totalSeconds // 3600
    totalSeconds = totalSeconds % 3600

    #then minutes and seconds
    minutePart = totalSeconds // 60
    secondPart = totalSeconds % 60

    #am/pm label
    if hour24 >= 12:
        meridiem = "PM"
    else:
        meridiem = "AM"

    #12 hour hour value
    hour12 = hour24 % 12
    if hour12 == 0:
        hour12 = 12

    #return final string
    return str(hour12) + " " + str(minutePart) + " " + str(secondPart) + " " + meridiem


#main program
rawSeconds = input("Enter the number of seconds since midnight: ")

#validate digit input
if not rawSeconds.isdigit():
    print("Input must be a non-negative integer.")
else:
    secValue = int(rawSeconds)

    finalTime = timeConversion(secValue)
    print("Converted Time:")
    print(finalTime)