import pandas as pd
data = [100, 102, 104, 106, 108]
series = pd.Series(data, index=['apartment #1', 'apartment #2', 'apartment #3', 'apartment #4', 'apartment #5'])

print(series)
print(series.loc["apartment #3"])  # Accessing a specific element using label

series.loc["apartment #3"] = 110  # Modifying a specific element using label
print(series)

print(series.iloc[2])  # Accessing a specific element using integer position

print(series[series >= 110])  # Filtering elements based on a condition


calories= {"Day 1": 420, "Day 2": 380, "Day 3": 390, "Day 4": 400, "Day 5": 410}
series2 = pd.Series(calories)
print(series2)

print(series2.loc["Day 3"])  # Accessing a specific element using label

series2.loc["Day 3"] = 395  # Modifying a specific element using label
print(series2)


print(series2[series2 <= 400])  # Filtering elements based on a condition



#dataframe = A tabular data structure with labeled axes (rows and columns). It is similar to a spreadsheet or SQL table, and it is one of the most commonly used data structures in pandas. A DataFrame can be created from various data sources such as lists, dictionaries, or external files like CSV or Excel.
data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Age": [25, 30, 35, 40, 45]}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5"])
print(df.loc["Employee 3"])  # Accessing a specific row using label

print(df.iloc[2])  # Accessing a specific row using integer position


#adding a new column to the DataFrame
df["Department"] = ["HR", "Finance", "IT", "Marketing", "Sales"]
print(df)

# adding a new row to the DataFrame
new_row = pd.DataFrame({"Name": ["Frank"], "Age": [50], "Department": ["Operations"]}, index=["Employee 6"])
df = pd.concat([df, new_row])
print(df)

#adding multiple new rows to the DataFrame
new_rows = pd.DataFrame({"Name": ["Grace", "Hannah"], "Age": [28, 32], "Department": ["Legal", "R&D"]}, index=["Employee 7", "Employee 8"])
df = pd.concat([df, new_rows])
print(df)