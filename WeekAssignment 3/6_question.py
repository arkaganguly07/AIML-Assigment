"""
Q6> Print the shape of the matrix from the previous part with .shape.
"""

import numpy as np

arr = np.arange(4)
mat = np.reshape(arr, (2, 2))

print(mat)
print(mat.shape)

# Output: [[0 1]
#         [2 3]]
# (2, 2)
