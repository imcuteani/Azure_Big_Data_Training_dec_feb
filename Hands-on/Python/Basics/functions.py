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

# bin() function is used to return the binary representation of any integer 

x = 10
y = bin(x)
print(y)

# boolean function 

test1 = [] 
print(test1, 'is', bool(test1))

test1 = [0]
print(test1, 'is', bool(test1))


test1 = 0.0
print(test1, 'is', bool(test1))

test1 = None
print(test1, 'is', bool(test1))

test1 = 'Hello Python'
print(test1, 'is', bool(test1))

# bytes() function is used to check over if the object passed can be called or not & returns the byte object. 

# byte() function in python can convert objects into byte objects, or it can create empty bytes objects of the specified size. 


string = "hello python"
array = bytes(string, 'utf-8')
print(array)


# compile() takes source code as input and returns the code object which can later be executed by exec() function

code_str = 'x = 5\ny = 10 \nprint("sum", x + y)'
code = compile(code_str, 'sum_py', 'exec')
print(type(code))
exec(code) 

x = 40
a = compile('x == 40', '', 'eval')
print(eval(a))

x = 60 

a = compile('x', 'test', 'single')
print(type(a))
exec(a)

# any() function returns true if any item in an iterable is true, else returns false. 

I = [4, 6, 8, 10]
print(any(I))

I = [0, False]
print(any(I))

# ASCII() function returns a string containing the printable representation of an object 

# ascii() function returns a readable version of any object (Strings, tuples, lists, etc.)

normalText = "Python is the most popular programming language in 2022"
print(ascii(normalText))

# bytearray() returns a bytearray object and can convert objects into bytearray objects, also it can create an empty
# bytearray object 

# bytearray() function in python returns a bytearray object. It can convert objects to bytearray objects. 
# the bytearray() function can create an empty bytearray objects of the specified size 

string = "python is a high level programming language"

arr = bytearray(string, 'utf-8')
print(arr)

# format() represents the formatted representation of the given value 

# the format() function formats the specified values and insert them inside the string's placeholder. 
# the placeholder is defined using the curly brackets in syntax. The format() method returns the formatted string. 

# float format 

print(format(126, "f"))

print(format(125,"b"))

# binary format

print(format(12,"b"))

txt1 = "The name of the person is {0} , his age is {1} ".format("John", 35)
print(txt1)

# Difference between byte() and bytearray() func in Py 

# the difference between byte() and bytearray() func is that byte() returns an object that cannot be modified. 
# the bytearray() returns an object which can be modified. 

# map() function is used to return a list of results after applying a given function to each item of an iterable(list, tuple) etc. 

def calculateAddition(n):
    return n + n

numbers = (1, 5)
result = map(calculateAddition, numbers)
print(result) 

# converting map object to an set 

numbersAddition = set(result)
print(numbersAddition)

# enumerate() function returns enumerated object 

result = enumerate([1, 2, 3])
print(result)
print(list(result))

# dict() function which is constructor helps to create a dictionary 
# if no arguments are passed, it creates an empty dictionary 
# if a positional arguments are given, a dictionary that it creates, with the same key-value pairs. 
# if any keyword arguments are given, the keyword arguments and their values are added to the dictionary which has been created from the positional argument. 

result = dict() 
result2 = dict(a = 1, b = 2)

print(result)
print(result2)

#filter() function is used to get filtered elements. This function actually takes two arguments. 
# first one is function and second one is the iterable. 
# the filter() function returns a sequence of those elements of iterable object which returns true value. 

def filterdata(x): 
    if x > 5:
        return x
        
result = filter(filterdata, (1, 2, 6))

# display the result 
print(list(result))



