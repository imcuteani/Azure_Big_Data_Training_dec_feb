#Python data types can be of four types: 
# Numeric -> Integer, Complex Number, Float 
# Dictionary -> Unordered set of key-value pairs of items. It's like associative array or a hash table where 
# each key stores a specific value. Keys can hold any primitive data types, whereas values is an arbitary python object. 
#

# Boolean -> true, false (specifies the condition as true or false)
# Set -> used it store unordered collection of list which is iterable, mutable and no duplicate elements. It's highly
# optimized with accessing a specific element contained in the set. 
# Sequence type -> String, List and Tuple 
# 
# Tuples are similar to lists , tuples in python can contain the collection of items of different data types. 
# Tuples are read-only data structure which we cant modify the size and the value of items of a tuple. 

# List is the most basic data structure in python. List is the mutable data structure where items can be added to list
# after the list creation.  
# a single list can contain strings, integers, other objects. 
# Lists in python can be used for creation of stacks and queues. 
# Lists can be mutable. 


# Difference between List and Tuple 
# a) List is mutable and tuple is immutable
# b) the implication of iterations is time-consuming in the list whereas the implications are much faster in tuples
# c) Operations like insertions, deletions are better performed with list. with Tuples, elements can be accessed better. 
# d) Lists consumes more meory and contains multiple built-in methods. Tuples consumes less memory and doesn't multiple built-in method.  

# Python creates a number object when a number is assigned to a variable 

a = 10 
print("The type of a: ", type(a))

b = 40.4 
print("The type of b: ", type(b))

c = 3 + 4j 
print("The type of c: ", type(c))
print("c is complex number: ", isinstance(3 + 4j, complex))

# string operations 

str = "Hello this is Python programming"
print(str)
hello = 'hello'
print(len(hello))
world = 'world'
hw = hello + ' ' + world  # string concatenation in python
print(hw) 

# apply string formatting with sprintf style 

hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)



