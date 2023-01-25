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

# Get a slice of list from start to index 2 (exclusive)

print(nums[:3])

# Get a slice of whole list in Python 

print(nums[:]) 

# Get a slice of whole list, slices can be negative 
print(nums[:-2])

# assign a new sublist to a slice 

nums[2:4] = [8,9]
print(nums)
 



