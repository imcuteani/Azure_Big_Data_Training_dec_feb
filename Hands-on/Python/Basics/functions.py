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





