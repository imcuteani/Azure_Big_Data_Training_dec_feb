import numpy as np 

a = np.array([[1, 4, 2],
             [3, 4, 6],
             [0, -1, 5]])


# sorting of array 

print("Array elements in sorted order:\n", np.sort(a, axis= None))

# sorting of array in Numpy row-wise 

print("Row-wise sorted array:\n", np.sort(a, axis=1))

# specify the sort algorithm 
print("Column wise sort algorithms by applying merge-sort:\n", np.sort(a, axis= 0, kind='mergsort'))

# example to show sorting of structured array 
# Structured array in Python Numpy is similar to Struct in C, Structured array in Numpy uses the data containers as fields. 
# each field contains data of any type and size. Array elements can be accessed with the help of dot notation. 

#dtypes = ([('name', (np.str_, 10), ('grad_year', np.int32))])

# values to be kept in the array 

#values = [('James', 2006), ('Alan', 2020), ('Paul', 2018), ('Andy', 2021)]

#creating array 

#arr = np.array(values, dtype=dtypes)

a = np.array([('James', 2006, 8.5), ('Alan', 2020, 8.5)], 
      dtype =[('name', (np.str_, 10)), ('grad_year', np.int32), ('cgpa', np.float64)])

print(a)


print("\nArray sorted by names:\n", np.sort(a, order='name'))

print("Array sorted by graduation year and then cgpa:\n", np.sort(a, order=['grad_year', 'cgpa']))

