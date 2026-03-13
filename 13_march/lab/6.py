# Question 6
# Create a 4×4 matrix and calculate:
# • Row-wise sum
# • Column-wise sum
# Example Matrix
# [[1 2 3 4]
# [5 6 7 8]
# [9 10 11 12]
# [13 14 15 16]]
# Expected Output
# Row Sum:
# [10 26 42 58]
# Column Sum:
# [28 32 36 40]

import numpy as np

mat = np.arange(1, 17).reshape(4, 4)
print("Matrix :\n", mat)
print("Row Sum :", mat.sum(axis=1))
print("Column Sum :", mat.sum(axis=0))