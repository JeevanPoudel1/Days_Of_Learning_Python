import pandas as pd

#data cleaning = process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset

df = pd.read_csv('pokemon.csv')


#1. Drop irrelevant features
df = df.drop(columns=['Total', 'Generation', 'Legendary'])
print(df.head())

df = df.dropna(subset=["Name"])  # drop rows with missing values in the "Name" column
print(df.to_string())  # print the entire DataFrame without truncation  

df = df.fillna({"Type 2": "Unknown"})  # fill missing values in the "Type 2" column with "Unknown"


print(df.to_string())  # print the entire DataFrame without truncation


df["type1"] = df["Type 1"].str.lower()  # convert the "Type 1" column to lowercase
df["type2"] = df["Type 2"].str.lower()  # convert the "Type 2" column to lowercase
df["type2"] = df["Type 1"].replace({"Grass": "grass", 
                                    "Fire": "fire", 
                                    "Water": "water"})  # replace specific values in the "Type 1" column


print(df.to_string())  # print the entire DataFrame without truncation


df["type1"] = df["Type 1"].str.lower()  # convert the "Type 1" column to lowercase
df["type2"] = df["Type 2"].str.lower()  # convert the "Type 2" column to lowercase
df["type2"] = df["Type 1"].replace({"Grass": "grass", 
                                    "Fire": "fire", 
                                    "Water": "water"})  # replace specific values in the "Type 1" column

#standardize the "Name" column by converting it to title case
df["Name"] = df["Name"].str.title()  # convert the "Name" column to title case
                                                                        
#fix data types
df["HP"] = df["HP"].astype(int)  # convert the "HP" column to integer data type



#removing duplicates
df = df.drop_duplicates()  # drop duplicate rows from the DataFrame

print(df.head())

