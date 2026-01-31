#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 question 3 Data 221
def computesexponent(x,y):
    #function that works to get exponent
    return x**y

pairs=[(1,2),(6,7),(3,-2),(10,2)]
#random pair of nums
unpackedpairs=[]
#list to store results for x,y pairs
for x,y in pairs:
#looping through each of the numbers unpacking x,y
    if y<0:
    #If the exponent y is -ve skip
        continue
    unpackedpairs.append(computesexponent(x,y))
#add result to the list computing x,y
print(unpackedpairs)
#prints the list