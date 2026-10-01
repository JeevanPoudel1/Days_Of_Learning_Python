from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[6]])

print("Prediction:", prediction[0])