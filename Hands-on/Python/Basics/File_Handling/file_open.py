# file handling operations in Python

# open() is used to open a file through python script

# "r" - Opens a file for reading. Returns error if the file doesn't exist. 
# "a" - Opens the files a file for appending. creates the file if it doesn't exist. 
# "w" - Opens a file for writing. Creates the file if it doesn't exist. 
# "x " - Creates the spcified file, returns an error if it doesn't exist. 
# "t"  - text (default value, text mode)
# "b" - binary mode (e.g. images)

f = open('new_text_doc.txt')
txt= f.read(10)  # read the first 10 characters 
#print(type(txt))
#print(txt)
f.close()

# returns the text line by line format / list of lines. 

f = open('new_file_read.txt', 'rt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()


# another way to open the file and also to close the files by itself. 

with open('new_file_read.txt', 'rt') as f: 
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)