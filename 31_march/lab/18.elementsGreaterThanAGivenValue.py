import numpy as np

array = np.array([10, 25, 15, 40, 35, 8, 50, 20])
target_value = 20

indices = np.where(array > target_value)

print("Array:", array)
print("Target value:", target_value)
print("Indices of elements > target:", indices[0])
print("Elements greater than target:", array[indices])
