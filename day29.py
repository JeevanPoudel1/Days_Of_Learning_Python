import numpy as np
import pandas as pd


# Student data
names = ["Alice", "Bob", "Charlie", "David", "Eva"]

marks = np.array([
    [85, 78, 92],
    [65, 70, 68],
    [90, 95, 88],
    [45, 55, 50],
    [75, 82, 80]
])

subjects = ["Python", "Math", "Database"]


# Create Pandas DataFrame
df = pd.DataFrame(marks, columns=subjects)

# Add student names
df["Name"] = names


# Calculate average using NumPy
df["Average"] = np.mean(marks, axis=1)


# Find Pass / Fail
df["Result"] = np.where(df["Average"] >= 50, "Pass", "Fail")


# Display complete data
print("\n===== STUDENT MARKS =====")
print(df)


# Statistics
print("\n===== STATISTICS =====")

print("Class Average:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))


# Find top student
top_student = df.loc[df["Average"].idxmax()]

print("\n===== TOP STUDENT =====")
print("Name:", top_student["Name"])
print("Average:", top_student["Average"])