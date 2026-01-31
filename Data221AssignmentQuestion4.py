#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 Question 4 Data 221
from random import random
#Generate 20 random values
values= [random() for i in range(20)]
#Generates random value between 0 and 1
xnum= random()
#Sorted values with the sort command
sortedvalues = sorted(values)
matchedindices = []
for i in range(len(sortedvalues)):\
#if index i is greater than or equal to xnum then i is a matching index
    if sortedvalues[i] >= xnum:
        matchedindices.append(i)
print("Sorted values:")
#prints sorted values
print(sortedvalues)
#print random x value comparing against
print("Compared value x:")
print(xnum)
if len(matchedindices) > 0:
    #if we found at least one matching index, print first
    print("First Matched index:")
    print(matchedindices[0])
else:
    #otherwise no values were>=xnum
    print("No Matching index(values are<x)")