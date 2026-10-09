import pandas as pd

df = pd.read_csv('pokemon.csv')

#showing non truncated data
#print(df.to_string())

print(df.head())
print(df.describe())
print(df.info())

#selection techniques
# selecting a single column
print(df['Name'])
print(df[['Name', 'Type 1']])
print(df[["Name", "Type 1"]].iloc[0:5]) # selecting rows and columns by index

print(df.iloc[0:5, 0:3]) # selecting rows and columns by index
#selecting a single row

fg = pd.read_csv("pokemon.csv", index_col='Name')
print(fg.iloc[0]) # selecting a single row by index
print(fg.loc["Bulbasaur", "Type 1"]) # selecting a single row by label
print(fg.loc[["Charizard", "Charmander"], "Type 1"]) # selecting multiple rows by label

print(fg.iloc[0:5, 0:3]) # selecting rows and columns by index
print(df.iloc[0:11:2, 0:3]) # selecting rows and columns by index with step