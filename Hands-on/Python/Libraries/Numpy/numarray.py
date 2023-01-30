# basic array characteristics 

import numpy as np 

# creating the array object 

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
# print the type of array object 
#
print("Array is of type: ", type(arr))

# printing the array dimension(axes)

print("No of Dimensions: ", arr.ndim)

#print shape of the array 

print("Shape of array: ", arr.shape)

# print size (total no of elements in array)

print("Size of array: ", arr.size)

# printing the type of elements in array 

print("Array stores elements of type: ", arr.dtype)

