#aggregate function = reduces a set of values down to a single value
#                       used to summarize data

import pandas as pd
df = pd.read_csv('pokemon.csv')


print(df['Attack'].sum())  # sum of all values in the 'Attack' column
print(df['Attack'].mean())  # mean of all values in the 'Attack' column
print(df['Attack'].max())  # maximum value in the 'Attack' column
print(df['Attack'].min())  # minimum value in the 'Attack' column
print(df['Attack'].count())  # count of all values in the 'Attack' column
print(df.mean(numeric_only=True))  # mean of all numeric columns

print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

#single column aggregate functions
print(df["Attack"].mean())
print(df["Attack"].sum())
print(df["Attack"].min())
print(df["Attack"].max())

#grouping data
grouped = df.groupby("Type 1")
print(grouped.mean(numeric_only=True))  # mean of all numeric columns for each group




group = df.groupby("Type 1")
print(group["Attack"].max())  # maximum of the 'Attack' column for each group
print(group["Attack"].count())
print(group["Attack"].sum())

