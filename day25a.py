import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original:", numbers)

print("First:", numbers[0])
print("Last:", numbers[-1])

print("First three:", numbers[:3])
print("Middle:", numbers[2:5])
print("From index 3:", numbers[3:])

print("Every second:", numbers[::2])
print("Reverse:", numbers[::-1])