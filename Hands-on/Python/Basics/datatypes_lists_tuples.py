# create a list in python 

xs = [3, 5, 7]
print(xs, xs[2])

# negative index on list which will count from the end of list 
print(xs[-1])
xs[2] = 'python'
print(xs)
xs.append('programming')
print(xs)

# remove and return the last element from list 
x = xs.pop() 
print(x, xs)

# Python lists slicing operation

nums = list(range(5))   #range is a built-in function which creates a list of integers 
print(nums)
print(nums[2:4])        # Get a slice from the index position of 2 to 4

# Get a slice from index 2 to end of list 
print(nums[2:]) 

# Get a slice of list from start to index 3 (exclusive)

print(nums[:3])

# Get a slice of whole list in Python 

print(nums[:]) 

# Get a slice of whole list, slices can be negative 
print(nums[:-2])

# assign a new sublist to a slice 

nums[2:4] = [8,9]
print(nums)

# List comprehension values 

# square of a number through python list 

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
    print(squares)


# even of square of numbers, to check whether the number is an even number or not     

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


# Python tuples 

# Tuples are unordered list of elements similar to list 



# Create a dictionary with tuple keys 

d = {(x, x + 1): x for x in range(10)}
#t = (5,7)
#print(type(t))
#print(d[t])           # print 5 
print(d[(1, 2)])      # print 1 (tuple key of first element of second index)

tupl = (1, "python", "programming", "spark", 4+5)
print(tupl)
print(tupl[3])



 



