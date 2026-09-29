# Complete end-to-end classification script using the Iris dataset and SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Initialize the Support Vector Classifier with a linear kernel
model = SVC(kernel='linear')

# Train the model
model.fit(X_train, y_train)

# Evaluate model performance
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"🎉 Model Accuracy: {accuracy * 100:.2f}%")
