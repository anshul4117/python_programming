# Question 4
# Create two 3×3 matrices and perform matrix multiplication.
# Matrix A
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
# Matrix B
# [[9 8 7]
# [6 5 4]
# [3 2 1]]
# Expected Output
# [[ 30 24 18]
# [ 84 69 54]
# [138 114 90]]

import numpy as np

mat_a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
mat_b = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

print("Matrix A :\n", mat_a)
print("Matrix B :\n", mat_b)
print("Matrix Multiplication :\n", np.dot(mat_a, mat_b))
