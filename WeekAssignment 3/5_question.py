"""
Q5> Make the matrix [[0, 1], [2, 3]] with np.arange and np.reshape.
"""

import numpy as np

arr = np.arange(4)
mat = np.reshape(arr, (2, 2))

print(mat)

# Output: [[0 1]
#         [2 3]]
