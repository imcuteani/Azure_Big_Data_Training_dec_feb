# Lambda function is a small, anomymous function without a name. It can have any number of arguments, but can have only
# one expression. 

# Lambda function is similar to anonymous function. 

from ctypes import c_ubyte

def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))

# Lets change the above function to a lambda function 

add_two_nums = lambda a, b: a + b
print(add_two_nums(5, 7))

# self-invoking lambda function 
add = (lambda a, b: a + b)(4, 6)
print(add)

square = lambda x : x ** 2 
print(square(60))
cube = lambda x : x ** 3
print(cube(108))

# passing multiple variables in lambda function

mul_variables = lambda a, b, c: a ** 2 - 3 * b + 4 * c 
print(mul_variables(7, 8, 9))

# invoking lambda function in Python inside of another function 

def power(x):
    return lambda n: x ** n 

cube = power(4) (5)
print(cube)
two_to_the_power_of_five = power(2)(5)
print(two_to_the_power_of_five)




