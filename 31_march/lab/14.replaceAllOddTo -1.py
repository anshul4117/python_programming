import numpy as np

# NumPy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a copy to modify
result = array.copy()

# Loop through and replace odd numbers
for i in range(len(result)):
    if result[i] % 2 != 0:
        result[i] = -1

print("Original array:", array)
print("Modified array:", result)