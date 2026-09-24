import pandas as pd
s = pd.Series([1,2,3,4], index = ['a','b','c','d'])
print(s)

df = pd.DataFrame({
    "name":["jeevan", "hridesh" ,"bibek", "keshab"],
    "marks":[100,99,80,84]
    })
print(df)

ab = pd.read_csv("students.csv")
print(ab)

print(ab.head())
print(ab.tail())
print(ab.describe())
print(ab.info())

#data selection
#print(df["id"])
#print(type(df["id"]))
#print[["id", "name of id"]]
#print(df.iloc[0])           #row
#print(type(df.iloc[0])) 

'''
if rows dowsnot have data

inplace = True #changes happens into the original file

print(df.dropna())
print(df.fillna(0, inplace=true)  #  original data changes
print(df2.fillna(0))    # fills with 0
df.rename(column = {"name that you want to change" : "SL"})


'''

