# Question 8
# Create a 3×3 matrix and calculate the transpose of the matrix.
# Matrix
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
# Expected Output
# [[1 4 7]
# [2 5 8]
# [3 6 9]]

import numpy as np

mat = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Matrix :\n", mat)
print("Transpose :\n", mat.T)
