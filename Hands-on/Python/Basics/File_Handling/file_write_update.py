# File write and update operations in Python 

# to write to an existing file, we must add a mode as a parameter to the open() function. 

#"a": append - will append to the end of the file. If the file does not exist, it will create a new file. 
# "w": write - will overwrite any existing content within the file. If the file doesn't exist, it'll create a new file. 


with open('new_file_read.txt', 'a') as f: 
   f.write('This text has to be appended to the end of the file')



# this method will create a new file if it doesn't exist in Write mode. 

with open('writing_file_sample.txt', 'w') as f: 
    f.write("This text will be written to this newly created file")
