import numpy as np

# 2D NumPy array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract diagonal elements
diagonal = np.diag(matrix)

print("Matrix:\n", matrix)
print("Diagonal elements:", diagonal)