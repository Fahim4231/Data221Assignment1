#Fahim Ahmadi
#January29 2026
#30268241 Assignment 1 Question 8 Data 221
import pandas as pd

#sample data
tableData = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

#build dataframe
df = pd.DataFrame(tableData)

#add computed column: A*B + C
df["Computed"] = (df["A"] * df["B"]) + df["C"]

#print result
print(df)