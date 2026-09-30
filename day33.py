import numpy as np
import pandas as pd


# ==========================================================
# STUDENT PERFORMANCE ANALYSIS SYSTEM
# ==========================================================

print("=" * 60)
print("       STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 60)


# ----------------------------------------------------------
# 1. CREATE DATA
# ----------------------------------------------------------

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack"
    ],

    "Python": [85, 72, 95, 60, 88, 76, 91, 55, 82, 68],

    "Math": [90, 65, 92, 58, 85, 70, 94, 50, 78, 72],

    "Database": [88, 70, 96, 62, 90, 75, 89, 52, 85, 65],

    "Networking": [82, 68, 94, 65, 87, 73, 92, 48, 80, 70],

    "Attendance": [95, 88, 98, 75, 92, 85, 96, 70, 89, 82]
}


df = pd.DataFrame(data)


print("\n===== ORIGINAL DATA =====")
print(df)


# ----------------------------------------------------------
# 2. CALCULATE TOTAL MARKS USING NUMPY
# ----------------------------------------------------------

subjects = ["Python", "Math", "Database", "Networking"]

df["Total"] = np.sum(df[subjects].values, axis=1)

df["Average"] = np.mean(df[subjects].values, axis=1)


# ----------------------------------------------------------
# 3. ASSIGN GRADES
# ----------------------------------------------------------

def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


df["Grade"] = df["Average"].apply(calculate_grade)


# ----------------------------------------------------------
# 4. PASS / FAIL
# ----------------------------------------------------------

df["Result"] = np.where(
    df["Average"] >= 50,
    "PASS",
    "FAIL"
)


# ----------------------------------------------------------
# 5. RANK STUDENTS
# ----------------------------------------------------------

df["Rank"] = df["Average"].rank(
    ascending=False,
    method="min"
).astype(int)


# ----------------------------------------------------------
# 6. DISPLAY COMPLETE RESULT
# ----------------------------------------------------------

print("\n===== STUDENT RESULTS =====")

print(
    df[
        [
            "Student_ID",
            "Name",
            "Total",
            "Average",
            "Grade",
            "Result",
            "Rank"
        ]
    ].sort_values("Rank")
)


# ----------------------------------------------------------
# 7. CLASS STATISTICS USING NUMPY
# ----------------------------------------------------------

averages = df["Average"].to_numpy()

print("\n===== CLASS STATISTICS =====")

print("Class Average :", np.mean(averages))
print("Highest Average:", np.max(averages))
print("Lowest Average :", np.min(averages))
print("Standard Deviation:", np.std(averages))


# ----------------------------------------------------------
# 8. HIGHEST PERFORMER
# ----------------------------------------------------------

top_student = df.loc[df["Average"].idxmax()]

print("\n===== TOP STUDENT =====")

print("Name   :", top_student["Name"])
print("Average:", top_student["Average"])
print("Grade  :", top_student["Grade"])


# ----------------------------------------------------------
# 9. LOWEST PERFORMER
# ----------------------------------------------------------

lowest_student = df.loc[df["Average"].idxmin()]

print("\n===== LOWEST STUDENT =====")

print("Name   :", lowest_student["Name"])
print("Average:", lowest_student["Average"])
print("Grade  :", lowest_student["Grade"])


# ----------------------------------------------------------
# 10. SUBJECT-WISE AVERAGE
# ----------------------------------------------------------

subject_average = df[subjects].mean()

print("\n===== SUBJECT-WISE AVERAGE =====")

print(subject_average)


# ----------------------------------------------------------
# 11. SUBJECT WITH HIGHEST CLASS AVERAGE
# ----------------------------------------------------------

best_subject = subject_average.idxmax()
best_subject_average = subject_average.max()

print("\nBest Subject:", best_subject)
print("Average Mark:", best_subject_average)


# ----------------------------------------------------------
# 12. STUDENTS ABOVE CLASS AVERAGE
# ----------------------------------------------------------

class_average = df["Average"].mean()

above_average = df[
    df["Average"] > class_average
]

print("\n===== STUDENTS ABOVE CLASS AVERAGE =====")

print(
    above_average[
        ["Name", "Average", "Grade"]
    ]
)


# ----------------------------------------------------------
# 13. STUDENTS WITH HIGH ATTENDANCE
# ----------------------------------------------------------

high_attendance = df[
    df["Attendance"] >= 90
]

print("\n===== HIGH ATTENDANCE STUDENTS =====")

print(
    high_attendance[
        ["Name", "Attendance", "Average"]
    ]
)


# ----------------------------------------------------------
# 14. GRADE DISTRIBUTION
# ----------------------------------------------------------

grade_distribution = df["Grade"].value_counts()

print("\n===== GRADE DISTRIBUTION =====")

print(grade_distribution)


# ----------------------------------------------------------
# 15. PASS / FAIL COUNT
# ----------------------------------------------------------

result_count = df["Result"].value_counts()

print("\n===== PASS / FAIL =====")

print(result_count)


# ----------------------------------------------------------
# 16. BEST STUDENT IN EACH SUBJECT
# ----------------------------------------------------------

print("\n===== BEST STUDENT IN EACH SUBJECT =====")

for subject in subjects:

    index = df[subject].idxmax()

    name = df.loc[index, "Name"]

    mark = df.loc[index, subject]

    print(f"{subject}: {name} ({mark})")


# ----------------------------------------------------------
# 17. SORT STUDENTS BY PERFORMANCE
# ----------------------------------------------------------

ranking = df.sort_values(
    by="Average",
    ascending=False
)

print("\n===== STUDENT RANKING =====")

print(
    ranking[
        ["Rank", "Name", "Average", "Grade"]
    ]
)


# ----------------------------------------------------------
# 18. NUMPY STATISTICS
# ----------------------------------------------------------

print("\n===== NUMPY STATISTICS =====")

for subject in subjects:

    marks = df[subject].to_numpy()

    print(f"\n{subject}")

    print("Mean  :", np.mean(marks))
    print("Median:", np.median(marks))
    print("Maximum:", np.max(marks))
    print("Minimum:", np.min(marks))
    print("Std Dev:", np.std(marks))


# ----------------------------------------------------------
# 19. SAVE DATA TO CSV
# ----------------------------------------------------------

df.to_csv(
    "student_performance_results.csv",
    index=False
)

print("\n✓ Results saved to:")
print("student_performance_results.csv")


# ----------------------------------------------------------
# 20. FINAL SUMMARY
# ----------------------------------------------------------

print("\n" + "=" * 60)

print("PROJECT SUMMARY")

print("=" * 60)

print("Total Students :", len(df))
print("Class Average  :", round(df["Average"].mean(), 2))
print("Passed         :", (df["Result"] == "PASS").sum())
print("Failed         :", (df["Result"] == "FAIL").sum())
print("Best Student   :", top_student["Name"])
print("Best Subject   :", best_subject)

print("=" * 60)