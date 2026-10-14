import numpy as np
import pandas as pd

# 1. Generate dummy data using NumPy
np.random.seed(42)  # Ensures reproducibility
data_size = 5

ids = np.arange(101, 101 + data_size)
scores_math = np.random.randint(60, 100, size=data_size)
scores_science = np.random.randint(65, 100, size=data_size)

# Calculate a metric using NumPy vectorized arithmetic
average_scores = (scores_math + scores_science) / 2

# 2. Structure data into a Pandas DataFrame
raw_data = {
    "StudentID": ids,
    "Math": scores_math,
    "Science": scores_science,
    "Average": average_scores,
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass"],  # Categorical sample
}

df = pd.DataFrame(raw_data)
print("--- Initial DataFrame ---")
print(df)

# 3. Clean and transform data using Pandas & NumPy together
# Let's apply a NumPy log function to create a new column
df["Math_Log"] = np.log(df["Math"])

# Use Pandas .loc for conditional filtering (e.g., students averaging above 80)
honors_students = df.loc[df["Average"] > 80]

print("\n--- Honors Students (Average > 80) ---")
print(honors_students)

# 4. Aggregate metrics
summary_stats = df[["Math", "Science"]].agg([np.mean, np.median, np.std])
print("\n--- Summary Statistics ---")
print(summary_stats)
