# sys modules are built-in module in python which is used to execute the OS/system operations in Py
# sys module can use all variables, functions, operators from the python runtime environment
import sys

#fetch maximum value 

max_value = sys.maxsize
print(max_value)
print(sys.version)
print(sys.path)
print(sys.modules)

# creates a list with max size in Py

import sys 

max_value = sys.maxsize

try: 
    list = range(max_value + 1)

 # print the length of the list 
    print(len(list))

    print("List successfully created")

except Exception as e:
    print(e)
    print("List creation unsuccessful")       


import os 
cwd = os.getcwd()   # get current working directory in Py 
print("Current working directory in Py: ", cwd)
os.chdir('../')        # change the directory 


# list the files and folders within the directory 

path = "/"
dir_list = os.listdir(path)

print("Files and Directories in: '", path,"' : ")

# print the list 
print(dir_list)