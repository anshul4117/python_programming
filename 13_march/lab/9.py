# Question 9
# Generate a NumPy array of 10 random numbers between 0 and 1 and normalize the array between 0
# and 1.
# Example Output
# Original Array:
# [0.54 0.21 0.87 0.12 0.63 ...]
# Normalized Array:
# [0.56 0.12 0.95 0.00 0.67 ...]
# (Values will vary.)

import numpy as np

arr = np.random.rand(10)
print("Original Array :", arr)
print("Normalized Array :", (arr - arr.min()) / (arr.max() - arr.min()))   