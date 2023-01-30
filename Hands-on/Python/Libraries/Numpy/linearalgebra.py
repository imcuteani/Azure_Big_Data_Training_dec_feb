# Linear algebra in Numpy 

# on Numpy array, we can perform rank, determinant, trace etc. of an array. 
# eigen values of metrics 
# matrix and vector operations 
# solve the linear equations, fourier transformations etc. 

import numpy as np 

arr = np.array([[6, 1, 1], 
               [4, -2, 5],
               [2, 8, 9] ])

print("Rank of array: ", np.linalg.matrix_rank(arr))

# print the trace of the array 

print("\n Trace of the array:\n", np.trace(arr))

# Determinant of the array 

print("\n Determinant of the array:\n", np.linalg.det(arr))

# inverse the matrix 

print("\nInverse the array:", np.linalg.inv(arr))

# Matrix arr to be raised to the power of 3 

print("\n Matrix arr is raised to pwer of 3:\n", np.linalg.matrix_power(arr, 3))

# Linear Equation through Numpy 

a = np.array([[1, 3], [2, 4]])
b = np.array([8, 16])

print(("Solutions of this linear equation is:\n", np.linalg.solve(a, b)))

# calculate the eigen value and right eigenvectors of a square array 

a = np.diag((1, 3, 5))

print("Array is: ", a)

# calculate the eigen value using the eig() function in Numpy 

c , d = np.linalg.eig(a)

print("Eigen value is :", c)
print("Eigen vector value is :", d)

