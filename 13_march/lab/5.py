# Create a NumPy array of numbers from 1 to 25 and reshape it into a 5×5 matrix.
# Extract the middle 3×3 sub-matrix.
# Expected Output
# [[ 7  8  9]
# [12 13 14]
# [17 18 19]]

import numpy as np

arr = np.arange(1, 26)
mat = arr.reshape(5, 5)
print("5x5 Matrix :\n", mat)

sub = mat[1:4, 1:4]
print("\nMiddle 3x3 Sub-Matrix :\n", sub)
