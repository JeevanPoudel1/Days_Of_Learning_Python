import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# ==========================================
# 1. LOAD DATA
# ==========================================

iris = load_iris()


# ==========================================
# 2. CREATE PANDAS DATAFRAME
# ==========================================

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target


print("\n===== IRIS DATASET =====")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# ==========================================
# 3. NUMPY INFORMATION
# ==========================================

X = iris.data
y = iris.target

print("\n===== NUMPY INFORMATION =====")

print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])

print("Mean of features:")
print(np.mean(X, axis=0))

print("Maximum values:")
print(np.max(X, axis=0))

print("Minimum values:")
print(np.min(X, axis=0))


# ==========================================
# 4. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\n===== DATA SPLIT =====")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 5. CREATE MODEL
# ==========================================

model = SVC(kernel="linear")


# ==========================================
# 6. TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)


# ==========================================
# 7. MAKE PREDICTIONS
# ==========================================

predictions = model.predict(X_test)


# ==========================================
# 8. EVALUATE MODEL
# ==========================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n===== MODEL RESULT =====")

print(f"Model Accuracy: {accuracy * 100:.2f}%")


# ==========================================
# 9. COMPARE ACTUAL VS PREDICTED
# ==========================================

result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print("\n===== PREDICTIONS =====")
print(result)


# ==========================================
# 10. PREDICT A NEW FLOWER
# ==========================================

new_flower = np.array([
    [5.1, 3.5, 1.4, 0.2]
])

prediction = model.predict(new_flower)

flower_name = iris.target_names[prediction[0]]

print("\n===== NEW FLOWER PREDICTION =====")

print("Measurements:", new_flower)
print("Predicted Species:", flower_name)