# The statistics module provides functions for mathematical statistics of numeric data 

from statistics import * 
ages = (20, 34, 45, 12, 22, 58, 79)
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# string module 
#string module is useful for many purpose 

import string 
print(string.ascii_letters)    #show up the letters in ASCII
print(string.digits)           # show up the characters in digit format
print(string.punctuation)      # show up all punctuations 

# Random module 

# import the random module which gives a random number between 0 to 0.9999... 

from random import random, randint

print(random())  # it does not take any arguments, it returns the value between 0 and 0.9999... 
print(randint(5, 25))   # it returns a random integer between [5, 25] inclusive
