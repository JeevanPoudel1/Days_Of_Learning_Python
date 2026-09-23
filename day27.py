import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari", "Gita"],
    "Age": [20, 21, 19, 22],
    "Marks": [75, 88, 65, 92]
}

df = pd.DataFrame(data)

print(df)

print(df["Marks"])


print(df[df["Marks"] > 80])
df.head()
df.tail()
df.shape
df.columns
print(df.shape)
