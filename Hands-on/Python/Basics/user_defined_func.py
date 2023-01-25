# def is the keyword used to create the custom function in py

# the function to check whether the given input object is negative or positive 

def sign(x): 
    if x > 0:
        return 'positive'
    elif x < 0: 
        return 'negative'
    else: 
        return 'neutral'
for x in [-1, 0, 1]:
    print(sign(x))      


# pass optimal arguments in a python function 


def hello(name, loud = False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s'  % name)  

hello('Roger')
hello('Fredrick', loud = True)

# Write a fibonacci series in py upto n 

def fib(n):   # write a fibonacci series upto n numbers 
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()

fib(2000)       


# Given an input string in python whether it's palindrome or not, a string is said to be palindrome if the reverse 
# of the string is the same as the original string. 

# find the reverse of the string
# check if the reverse and the original string are same or not 

# using lists and reverse() method to check whether a given input string is palindrome or not 

# the extend() function adds the specified list of elements (or any other iterable) to the end of the current list 


def isPalindrome(s):
    x = list(s)
    y = []
    y.extend(x)
    x.reverse()
    if (x == y):
        return True
    return False


 # driver code block 
 

s = "malayalam"
a = "python"
val = isPalindrome(s)
val1 = isPalindrome(a)

if val1:
    print("Yes, the string is palindrome")
else: 
    print("No, the given input string is not a palindrome")   


              