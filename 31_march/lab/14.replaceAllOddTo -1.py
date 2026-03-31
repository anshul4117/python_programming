import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = array.copy()

for i in range(len(result)):
    if result[i] % 2 != 0:
        result[i] = -1

print("Original array:", array)
print("Modified array:", result)