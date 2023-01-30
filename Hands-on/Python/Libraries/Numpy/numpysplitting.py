# Numpy splitting

import numpy as np 

a = np.array([[1, 2, 5, 7, 9 , 14],
             [2, 4, 7, 8, 10, 16]])

# splitting into horizontal axis
# 

print("Splitting along with horizontal axis into two parts:\n ", np.hsplit(a, 2))

# Splitting into vertical axis 

print("Splitting into vertical axis into 2 parts:\n ", np.vsplit(a, 2))

