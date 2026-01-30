#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 Data 221
print("Question1:")
consecutivenumber=1
threshold=20
product=1
#Initalize variables with Descriptive names
while not (product*consecutivenumber)>threshold:
    product=product*consecutivenumber
    consecutivenumber=consecutivenumber+1
    print("Product is",product)
    print("Consecutivenumber is",consecutivenumber)

#Question 3
print("Question3:")
def computesexponent(x,y):
    return x**y

pairs=[(1,2),(6,7),(3,-2),(10,2)]
unpackedpairs=[]
for x,y in pairs:
    if y<0:
        continue
    unpackedpairs.append(computesexponent(x,y))
    print(unpackedpairs)

print("Question 4:")
