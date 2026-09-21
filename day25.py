import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)

# Basic information
print("Size:", numbers.size)
print("Shape:", numbers.shape)
print("Data type:", numbers.dtype)

# Mathematical operations
print("Add 10:", numbers + 10)
print("Multiply by 2:", numbers * 2)
print("Square:", numbers ** 2)

# Basic calculations
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# Create a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix:")
print(matrix)

print("Matrix shape:", matrix.shape)

# Access elements
print("First element:", matrix[0, 0])
print("Second row:", matrix[1])
print("First column:", matrix[:, 0])