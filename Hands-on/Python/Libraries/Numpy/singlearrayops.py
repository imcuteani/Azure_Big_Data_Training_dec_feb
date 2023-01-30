# Numpy array operations 

import numpy as np 

a = np.array([1, 2, 3, 5])

# add 1 to every element of the array 

print("Adding 1 to every element of the array: ", a+1)

# substraction 3 from every element 

print("Substraction 3 from each element: ", a-3)

# Multiply each element with 5 

print("multiplying each element by 5: ", a*5)

# Division each element with 1 

print("Dividing each element by 1: ", a/1)

#square each element 

print("Squaring each element: ", a**2)

# Modify the existing array 

a *= 2
print("Doubled each element of the original array: ", a)

# transpose an array 

a = np.array([[1, 2, 3], [4, 5, 6], [9, 6, 0]])
print("\nOriginal Array:\n", a)
print("Transpose of array", a.T)