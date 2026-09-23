import pandas as pd

data = {
    "Name": ["Alex", "John", "Sara", "Maya", "David"],
    "Age": [22, 25, 21, 27, 24],
    "Salary": [25000, 30000, 22000, 40000, 28000]
}

df = pd.DataFrame(data)
df["City"] = ["Kathmandu", "Pokhara", "Dharan", "Biratnagar", "Butwal"]

print(df)