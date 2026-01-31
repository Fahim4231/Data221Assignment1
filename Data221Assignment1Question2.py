#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 Question 2 Data 221
def buildingsummary(stringlist):
    #function with paramater stringlist
    summarystring = {}
    #summarystring in input list
    for text in stringlist:
        #Find the length of the current string
        text_length = len(text)
        #Decide if the length is even or odd
        length_parity = "even" if text_length % 2 == 0 else "odd"
        #If length % 2 ==0 it is even
        summarystring[text] = {"length": text_length, "parity": length_parity}

    return summarystring
    #return completed string


example_strings = ["data", "science"]
print(buildingsummary(example_strings))