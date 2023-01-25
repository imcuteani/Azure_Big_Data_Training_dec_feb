# Dictionaries in Python 

d = {'math' : 'algebra', 'chem' : 'experiment', 'phys': 'laws', 'stat' : 'variation'}
print(d['chem'])

# to check if a dictionary contains a specific key 
print('java' in d)

# add a new key in dictionary of Python 
d['bio'] = 'biology'
print(d['bio'])
print(d.get('bio', 'N/A')) # get an element with a default 

#delete an element from this dictionary 
del d['chem']
print(d.get('chem', 'N/A'))  # 'chem' is not longer a key, prints 'N/A'

# Looping over dictionaries for iteration

dict = {'person' : 2, 'cat' : 4, 'spider' : 8}
for animal in dict: 
    legs = dict[animal]
    print('A %s has %d legs' % (animal, legs))


# Sets are the underordered collection of distinct elements in Python

# Sets as the unordered collection of datatype which is iterable, mutable and has no duplicate elements

# The major advantage of Set is that highly optimized method for checking whether a specific element is contained in the set. 

# Set is based on data structure known as hash table. Since, sets are unordered, we can't access items using indexes as we can perform using lists. 

#typecasting of lists to set 

myset = set(["apple", "banana", "cherry"])
print(myset)

# adding an element 
myset.add("fig")
print(myset)

# frozen Sets in Python 

# Frozen sets in python refers to the immutable objects which only supports method and operators which produce 
# a result without affecting the frozen set or sets in which it's applied. 

# while the elements of a set can be modified at any time, elements of the frozen set remain the same after creation

# if no parameters are passed, it returns an empty frozenset


normal_set = set(["apple", "banana", "cherry"])
print(normal_set)


# a frozen set 
# a frozenset() method creates an immutable Set object from an iterable. It's a built-in python function. 
# As it is a Set object, he  
frozen_set = frozenset(["mango", "lichie", "pineapple", "starapple"])
print("\nFrozenSet")
print(frozen_set)


animals = {'cat', 'dog'}
print('cat' in animals)  # checks is an element is a set, prints true
print('fish' is animals) # checks whether the fish element is present, if not shows false. 
animals.add('fish')
print('fish' in animals) # prints as true
print(len(animals))
animals.remove('cat')
print(len(animals))

# For Loop over Set data type in Python 

animals = {'cat', 'dog', 'leopard'} 
for id, animal in enumerate(animals):
    print('%d: %s' % (id + 1, animal))

    

 











