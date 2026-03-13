# Question 7
# Create a NumPy array of numbers from 1 to 15 and find all numbers greater than 10.
# Expected Output
# [11 12 13 14 15]

import numpy as np

arr = np.arange(1, 16)
print("Array :", arr)
print("Numbers greater than 10 :", arr[arr > 10])