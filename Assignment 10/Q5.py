# Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).
import numpy as np


arr = np.array(['abc', 'def', 'ghi', 'jkl'])


width = 15

# Centered
centered = np.array([s.center(width, '_') for s in arr])
print("Centered:\n", centered)

# Left-justified
left_justified = np.array([s.ljust(width, '_') for s in arr])
print("\nLeft-Justified:\n", left_justified)

# Right-justified
right_justified = np.array([s.rjust(width, '_') for s in arr])
print("\nRight-Justified:\n", right_justified)