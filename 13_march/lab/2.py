# Question 2
# Create a 5×5 matrix with random integers between 1 and 100 and find:
# • Minimum value
# • Maximum value
# Example Output
# Matrix:
# [[23 45 12 89 34]
# [67 11 90 54 32]
# [76 28 19 47 65]
# [14 73 52 39 81]
# [60 21 48 70 16]]
# Min = 11
# Max = 90
# (Values may vary because of random numbers.)

import numpy as np

mat = np.random.randint(1, 101, size=(5, 5))
print("Matrix :\n", mat)
print("Min =", np.min(mat))
print("Max =", np.max(mat))
