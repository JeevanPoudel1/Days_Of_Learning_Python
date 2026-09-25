import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Create data
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "result": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}


# 2. Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)


# 3. Separate features and target
X = df[["study_hours"]]
y = df["result"]


# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Create model
model = LogisticRegression()


# 6. Train model
model.fit(X_train, y_train)


# 7. Test model
predictions = model.predict(X_test)

print("\nPredictions:", predictions)
print("Actual:", y_test.values)


# 8. Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy * 100, "%")


# 9. Predict a new student
new_student = np.array([[6.5]])

prediction = model.predict(new_student)


if prediction[0] == 1:
    print("\n6.5 hours → Predicted PASS")
else:
    print("\n6.5 hours → Predicted FAIL")