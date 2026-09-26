import pandas as pd
import numpy as np


# ============================================================
# 1. CREATE DATA
# ============================================================

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": [
        " Alice ",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Henry"
    ],
    "department": [
        "CS", "CS", "IT", "IT",
        "CS", "IT", "CS", "IT"
    ],
    "age": [20, 21, 19, 22, 20, 21, 19, 23],
    "gender": [
        "Female", "Male", "Male", "Male",
        "Female", "Male", "Female", "Male"
    ],
    "admission_date": [
        "2025-01-10",
        "2025-01-12",
        "2025-01-15",
        "2025-01-20",
        "2025-01-25",
        "2025-02-01",
        "2025-02-05",
        "2025-02-10"
    ]
})


marks = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "python": [85, 72, 90, 65, 95, 70, 88, 60],
    "math": [90, 75, 85, 70, 92, 68, 84, 55],
    "database": [88, 80, 87, 72, 94, 75, 90, 65]
})


# ============================================================
# 2. BASIC DATAFRAME / SERIES
# ============================================================

print("\n========== DATAFRAME ==========")
print(students)

print("\n========== SERIES ==========")
print(students["name"])

print("\n========== FIRST 5 ROWS ==========")
print(students.head())

print("\n========== LAST 5 ROWS ==========")
print(students.tail())

print("\n========== SHAPE ==========")
print(students.shape)

print("\n========== COLUMNS ==========")
print(students.columns)

print("\n========== DATA TYPES ==========")
print(students.dtypes)

print("\n========== INFORMATION ==========")
students.info()

print("\n========== STATISTICS ==========")
print(students.describe())


# ============================================================
# 3. CLEANING
# ============================================================

# Remove unnecessary spaces
students["name"] = students["name"].str.strip()

# Convert to lowercase
students["department"] = students["department"].str.lower()

# Convert department back to uppercase
students["department"] = students["department"].str.upper()

# Convert gender to category
students["gender"] = students["gender"].astype("category")


# ============================================================
# 4. DATETIME
# ============================================================

students["admission_date"] = pd.to_datetime(
    students["admission_date"]
)

students["year"] = students["admission_date"].dt.year
students["month"] = students["admission_date"].dt.month
students["day"] = students["admission_date"].dt.day
students["day_name"] = students["admission_date"].dt.day_name()


# ============================================================
# 5. MERGE DATA
# ============================================================

df = pd.merge(
    students,
    marks,
    on="student_id",
    how="inner"
)

print("\n========== MERGED DATA ==========")
print(df)


# ============================================================
# 6. INDEXING
# ============================================================

print("\n========== COLUMN ==========")
print(df["name"])

print("\n========== MULTIPLE COLUMNS ==========")
print(df[["name", "department", "python"]])

print("\n========== LOC ==========")
print(df.loc[0, "name"])

print("\n========== ILOC ==========")
print(df.iloc[0, 2])


# ============================================================
# 7. BOOLEAN FILTERING
# ============================================================

print("\n========== PYTHON > 80 ==========")
print(df[df["python"] > 80])

print("\n========== PYTHON > 80 AND MATH > 80 ==========")
print(
    df[
        (df["python"] > 80) &
        (df["math"] > 80)
    ]
)

print("\n========== CS OR IT ==========")
print(
    df[
        df["department"].isin(["CS", "IT"])
    ]
)

print("\n========== QUERY ==========")
print(
    df.query("python >= 80 and math >= 80")
)


# ============================================================
# 8. CALCULATIONS
# ============================================================

df["total"] = (
    df["python"] +
    df["math"] +
    df["database"]
)

df["average"] = (
    df["total"] / 3
)

print("\n========== TOTAL AND AVERAGE ==========")
print(
    df[
        ["name", "total", "average"]
    ]
)


# ============================================================
# 9. GRADING
# ============================================================

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "F"


df["grade"] = df["average"].apply(calculate_grade)

print("\n========== GRADES ==========")
print(
    df[
        ["name", "average", "grade"]
    ]
)


# ============================================================
# 10. PASS / FAIL
# ============================================================

df["status"] = np.where(
    df["average"] >= 60,
    "Pass",
    "Fail"
)

print("\n========== STATUS ==========")
print(
    df[
        ["name", "average", "status"]
    ]
)


# ============================================================
# 11. SORTING
# ============================================================

print("\n========== SORT BY AVERAGE ==========")

sorted_df = df.sort_values(
    "average",
    ascending=False
)

print(
    sorted_df[
        ["name", "average"]
    ]
)


# ============================================================
# 12. RANKING
# ============================================================

df["rank"] = (
    df["average"]
    .rank(
        ascending=False,
        method="dense"
    )
)

print("\n========== RANK ==========")
print(
    df[
        ["name", "average", "rank"]
    ]
)


# ============================================================
# 13. GROUPBY
# ============================================================

print("\n========== DEPARTMENT AVERAGE ==========")

department_average = (
    df.groupby("department")["average"]
    .mean()
)

print(department_average)


print("\n========== DEPARTMENT MAX ==========")

print(
    df.groupby("department")["average"]
    .max()
)


# ============================================================
# 14. GROUPBY + AGG
# ============================================================

summary = (
    df.groupby("department")
    .agg(
        average_marks=("average", "mean"),
        highest_marks=("average", "max"),
        lowest_marks=("average", "min"),
        students=("student_id", "count")
    )
)

print("\n========== DEPARTMENT SUMMARY ==========")
print(summary)


# ============================================================
# 15. TRANSFORM
# ============================================================

df["department_average"] = (
    df.groupby("department")["average"]
    .transform("mean")
)

df["difference_from_department_average"] = (
    df["average"] -
    df["department_average"]
)

print("\n========== TRANSFORM ==========")

print(
    df[
        [
            "name",
            "department",
            "average",
            "department_average",
            "difference_from_department_average"
        ]
    ]
)


# ============================================================
# 16. STRING OPERATIONS
# ============================================================

df["name_upper"] = df["name"].str.upper()

df["name_length"] = df["name"].str.len()

print("\n========== STRING OPERATIONS ==========")

print(
    df[
        ["name", "name_upper", "name_length"]
    ]
)


# ============================================================
# 17. MISSING DATA
# ============================================================

df.loc[0, "bonus"] = np.nan
df.loc[3, "bonus"] = np.nan

print("\n========== MISSING VALUES ==========")
print(df.isna().sum())

df["bonus"] = df["bonus"].fillna(5)

print("\n========== AFTER FILLING ==========")
print(df["bonus"])


# ============================================================
# 18. FINAL SCORE
# ============================================================

df["final_score"] = (
    df["average"] +
    df["bonus"]
)

print("\n========== FINAL SCORE ==========")

print(
    df[
        ["name", "average", "bonus", "final_score"]
    ]
)


# ============================================================
# 19. PIVOT TABLE
# ============================================================

print("\n========== PIVOT TABLE ==========")

pivot = pd.pivot_table(
    df,
    index="department",
    values=[
        "python",
        "math",
        "database",
        "average"
    ],
    aggfunc="mean"
)

print(pivot)


# ============================================================
# 20. MELT
# ============================================================

print("\n========== MELT ==========")

long_data = df.melt(
    id_vars=["student_id", "name"],
    value_vars=[
        "python",
        "math",
        "database"
    ],
    var_name="subject",
    value_name="marks"
)

print(long_data)


# ============================================================
# 21. CONCAT
# ============================================================

extra_students = pd.DataFrame({
    "student_id": [9, 10],
    "name": ["Iris", "Jack"],
    "department": ["CS", "IT"],
    "age": [20, 22]
})

combined = pd.concat(
    [
        students,
        extra_students
    ],
    ignore_index=True
)

print("\n========== CONCAT ==========")
print(combined)


# ============================================================
# 22. MULTI-INDEX
# ============================================================

multi_index_df = df.set_index(
    ["department", "student_id"]
)

print("\n========== MULTI INDEX ==========")
print(multi_index_df)


# ============================================================
# 23. RESET INDEX
# ============================================================

reset_df = multi_index_df.reset_index()

print("\n========== RESET INDEX ==========")
print(reset_df.head())


# ============================================================
# 24. ROLLING WINDOW
# ============================================================

df["rolling_average"] = (
    df["average"]
    .rolling(3)
    .mean()
)

print("\n========== ROLLING AVERAGE ==========")

print(
    df[
        ["name", "average", "rolling_average"]
    ]
)


# ============================================================
# 25. MEMORY USAGE
# ============================================================

print("\n========== MEMORY USAGE ==========")

print(
    df.memory_usage(
        deep=True
    )
)


# ============================================================
# 26. METHOD CHAINING
# ============================================================

result = (
    df
    .query("average >= 70")
    .assign(
        performance=lambda x:
        x["average"] / 100
    )
    .sort_values(
        "average",
        ascending=False
    )
)

print("\n========== METHOD CHAINING ==========")

print(
    result[
        [
            "name",
            "average",
            "performance"
        ]
    ]
)


# ============================================================
# 27. TOP STUDENTS
# ============================================================

top_students = (
    df.nlargest(
        3,
        "average"
    )
)

print("\n========== TOP 3 STUDENTS ==========")

print(
    top_students[
        ["name", "average", "rank"]
    ]
)


# ============================================================
# 28. SUBJECT STATISTICS
# ============================================================

subjects = [
    "python",
    "math",
    "database"
]

subject_statistics = df[subjects].agg(
    [
        "mean",
        "median",
        "min",
        "max",
        "std"
    ]
)

print("\n========== SUBJECT STATISTICS ==========")

print(subject_statistics)


# ============================================================
# 29. CORRELATION
# ============================================================

print("\n========== CORRELATION ==========")

print(
    df[
        [
            "python",
            "math",
            "database",
            "average"
        ]
    ].corr()
)


# ============================================================
# 30. EXPORT
# ============================================================

df.to_csv(
    "student_analysis.csv",
    index=False
)

df.to_excel(
    "student_analysis.xlsx",
    index=False
)

print("\n========== FILES CREATED ==========")
print("student_analysis.csv")
print("student_analysis.xlsx")


# ============================================================
# FINAL DATA
# ============================================================

print("\n========== FINAL DATASET ==========")

print(
    df[
        [
            "student_id",
            "name",
            "department",
            "python",
            "math",
            "database",
            "total",
            "average",
            "grade",
            "status",
            "rank",
            "final_score"
        ]
    ]
)