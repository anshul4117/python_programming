import numpy as np

array = np.array([10, 20, 30, 40, 50, 60, 70, 80])

min_val = np.min(array)
max_val = np.max(array)

normalized = (array - min_val) / (max_val - min_val)

print("Original array:", array)
print("Normalized array:", normalized)