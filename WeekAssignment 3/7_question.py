"""
Q7> Print the number of rows in the matrix from part 5 with .shape.
"""

import numpy as np

arr = np.arange(4)
mat = np.reshape(arr, (2, 2))
rows = mat.shape[0]

# print(mat)
print("Number of rows: ", rows)

# Output: Number of rows:  2
