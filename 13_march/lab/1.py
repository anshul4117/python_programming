#generate
#  Create a NumPy array of numbers from 1 to 20 and reshape it into a 4×5 matrix.
# Expected Output
# [[ 1 2 3 4 5]
# [ 6 7 8 9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]]

import numpy as np

arr = np.arange(1, 21)
mat = arr.reshape(4, 5)
print("4x5 Matrix :\n", mat)