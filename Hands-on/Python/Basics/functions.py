# Functions in Python 

# abs() function is used to return the absolute value of number 

integer = - 200
print('Absolute value is: ', abs(integer))

floating = - 30.67
print('Absolute value is: ', abs(floating))

# all() function is python is a kind of function which accepts an iterable object (list, dictionary etc.). It returns
# true if all items in passed returned are true. 
# otherwise, it returns false. 

k = [3, 6, 9, 12]
print(all(k))

# all values are false 

k = [0, False]
print(all(k))


# one true value to show 

k = [1, 3, 7, 10]
print(all(k))

# one false value to show 

k = [1, False, 7, 10]
print(all(k))

# empty iterable value 

k = []
print(all(k))